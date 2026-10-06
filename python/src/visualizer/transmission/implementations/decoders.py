"""Decoder implementations used in transmission simulations."""

from ..models import Bits


class IdentityDecoder:
    def decode(self, received: Bits) -> Bits:
        raise NotImplementedError("Implement the identity decoder.")


class MajorityVoteDecoder:
    def decode(self, received: Bits) -> Bits:
        raise NotImplementedError("Implement the majority-vote decoder.")
