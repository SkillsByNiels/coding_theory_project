"""Encoder implementations used in transmission simulations."""

from ..models import Bits


class IdentityEncoder:
    def encode(self, message: Bits) -> Bits:
        raise NotImplementedError("Implement the identity encoder.")


class TripleRepetitionEncoder:
    def encode(self, message: Bits) -> Bits:
        raise NotImplementedError("Implement the triple-repetition encoder.")
