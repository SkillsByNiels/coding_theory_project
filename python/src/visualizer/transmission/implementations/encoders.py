"""Encoder implementations used in transmission simulations."""

from ..models import Bits


class IdentityEncoder:
    def encode(self, message: Bits) -> Bits:
        return message


class TripleRepetitionEncoder:
    def encode(self, message: Bits) -> Bits:
        return tuple(bit for bit in message for _ in range(3))
