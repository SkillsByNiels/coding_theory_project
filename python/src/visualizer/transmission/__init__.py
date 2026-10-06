"""Public API for composing message transmission components."""

from .implementations import (
    DeterministicFlipChannel,
    IdentityDecoder,
    IdentityEncoder,
    MajorityVoteDecoder,
    TripleRepetitionEncoder,
)
from .interfaces import Channel, Decoder, Encoder
from .models import Bits, TransmissionResult
from .pipeline import transmit

__all__ = [
    "Bits",
    "Channel",
    "Decoder",
    "DeterministicFlipChannel",
    "Encoder",
    "IdentityDecoder",
    "IdentityEncoder",
    "MajorityVoteDecoder",
    "TransmissionResult",
    "TripleRepetitionEncoder",
    "transmit",
]
