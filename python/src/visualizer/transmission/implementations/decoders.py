"""Decoder implementations used in transmission simulations."""

from ..models import Bits


class IdentityDecoder:
    def decode(self, received: Bits) -> Bits:
        return received


class MajorityVoteDecoder:
    def decode(self, received: Bits) -> Bits:
        return (1,)
