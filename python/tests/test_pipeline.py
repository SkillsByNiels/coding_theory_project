from visualizer.transmission import TransmissionResult, transmit


class RecordingEncoder:
    def __init__(self) -> None:
        self.calls: list[tuple[int, ...]] = []

    def encode(self, message: tuple[int, ...]) -> tuple[int, ...]:
        self.calls.append(message)
        return (1, 1, 0)


class RecordingChannel:
    def __init__(self) -> None:
        self.calls: list[tuple[int, ...]] = []

    def transmit(self, encoded: tuple[int, ...]) -> tuple[int, ...]:
        self.calls.append(encoded)
        return (1, 0, 0)


class RecordingDecoder:
    def __init__(self) -> None:
        self.calls: list[tuple[int, ...]] = []

    def decode(self, received: tuple[int, ...]) -> tuple[int, ...]:
        self.calls.append(received)
        return (1, 0)


def test_transmit_passes_each_stage_output_forward_once() -> None:
    encoder = RecordingEncoder()
    channel = RecordingChannel()
    decoder = RecordingDecoder()
    message = (1, 0)

    result = transmit(message, encoder, channel, decoder)

    assert encoder.calls == [message]
    assert channel.calls == [(1, 1, 0)]
    assert decoder.calls == [(1, 0, 0)]
    assert result == TransmissionResult(
        message=message,
        encoded=(1, 1, 0),
        received=(1, 0, 0),
        decoded=(1, 0),
    )
