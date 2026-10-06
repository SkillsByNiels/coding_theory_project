"""Shared data types for a transmission."""

from dataclasses import dataclass
from typing import TypeAlias

Bits: TypeAlias = tuple[int, ...]


@dataclass(frozen=True)
class TransmissionResult:
    message: Bits
    encoded: Bits
    received: Bits
    decoded: Bits
