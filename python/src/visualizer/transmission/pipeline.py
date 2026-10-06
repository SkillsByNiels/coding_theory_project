"""Functions for connecting transmission components."""

from .interfaces import Channel, Decoder, Encoder
from .models import Bits, TransmissionResult


def transmit(
    message: Bits,
    encoder: Encoder,
    channel: Channel,
    decoder: Decoder,
) -> TransmissionResult:
    raise NotImplementedError("Implement the message transmission pipeline.")
