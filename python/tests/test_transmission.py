from binascii import Error
from typing import cast

import pytest

from visualizer.transmission import (
    Bits,
    DeterministicFlipChannel,
    IdentityDecoder,
    IdentityEncoder,
    MajorityVoteDecoder,
    TransmissionResult,
    TripleRepetitionEncoder,
    transmit,
)


def test_identity_pipeline_delivers_message_without_channel_errors() -> None:
    message = (1, 0, 1)

    result = transmit(
        message,
        IdentityEncoder(),
        DeterministicFlipChannel(),
        IdentityDecoder(),
    )
    print(result)

    assert result == TransmissionResult(
        message=message,
        encoded=message,
        received=message,
        decoded=message,
    )


def test_channel_flips_the_requested_bit() -> None: 
    channel = DeterministicFlipChannel(flip_positions=(1, 0, 0))

    assert channel.transmit((1, 0, 1)) == (0, 0, 1 )


def test_channel_flips_the_requested_mod2() -> None:
    channel = DeterministicFlipChannel(flip_positions=(1, 0, 1))

    assert channel.transmit((1, 0, 1)) == (0, 0, 1)

def test_correct_tuple_size_DeterministicFlipChannel() -> None:
    result = transmit(
        (1, 0, 1),
        IdentityEncoder(),
        DeterministicFlipChannel(flip_positions=(1,0,1,0)),
        IdentityDecoder(),
    )
    assert result.decoded == "Encoded message length 3 does not match flip positions length 4."

def test_TripleRepetitionEncoder_encodes_1() -> None:
    message = (1,)

    result = transmit(
        message,
        TripleRepetitionEncoder(),
        DeterministicFlipChannel(),
        IdentityDecoder(),
    )

    assert result.encoded == (1, 1, 1)
    assert result.received == (1, 1, 1)
    assert result.decoded == message

def test_triple_repetition_corrects_one_error_in_each_block() -> None:
    result = transmit(
        (1, 0),
        TripleRepetitionEncoder(),
        DeterministicFlipChannel(flip_positions=(1, 5)),
        MajorityVoteDecoder(),
    )

    assert result.encoded == (1, 1, 1, 0, 0, 0)
    assert result.received == (1, 0, 1, 0, 0, 1)
    assert result.decoded == (1, 0)


def test_triple_repetition_can_fail_with_two_errors_in_one_block() -> None:
    result = transmit(
        (1,),
        TripleRepetitionEncoder(),
        DeterministicFlipChannel(flip_positions=(0, 1)),
        MajorityVoteDecoder(),
    )

    assert result.received == (0, 0, 1)
    assert result.decoded == (0,)


def test_majority_decoder_rejects_incomplete_repetition_block() -> None:
    with pytest.raises(ValueError, match="multiple of 3"):
        MajorityVoteDecoder().decode((1, 1))


def test_channel_rejects_flip_position_outside_transmission() -> None:
    with pytest.raises(ValueError, match="outside the transmitted message"):
        DeterministicFlipChannel(flip_positions=(3,)).transmit((1, 0, 1))


def test_transmission_rejects_values_that_are_not_bits() -> None:
    with pytest.raises(ValueError, match="only 0 and 1"):
        transmit(
            cast(Bits, (0, 1.0)),
            IdentityEncoder(),
            DeterministicFlipChannel(),
            IdentityDecoder(),
        )
