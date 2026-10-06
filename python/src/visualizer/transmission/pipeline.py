"""Functions for connecting transmission components."""

from .interfaces import Channel, Decoder, Encoder
from .models import Bits, TransmissionResult


def transmit(
    message: Bits,
    encoder: Encoder,
    channel: Channel,
    decoder: Decoder,
) -> TransmissionResult:
    return TransmissionResult(message,
                              encoder.encode(message),
                              channel.transmit(encoder.encode(message)),
                              decoder.decode(channel.transmit(encoder.encode(message)))
    )