"""Interfaces implemented by transmission pipeline components."""

from typing import Protocol

from .models import Bits


class Encoder(Protocol):
    def encode(self, message: Bits) -> Bits: ...


class Channel(Protocol):
    def transmit(self, encoded: Bits) -> Bits: ...


class Decoder(Protocol):
    def decode(self, received: Bits) -> Bits: ...
