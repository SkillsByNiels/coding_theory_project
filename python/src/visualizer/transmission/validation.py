"""Validation helpers shared by transmission components."""

from .models import Bits


def _checked_bits(bits: Bits) -> Bits:
    result = tuple(bits)
    if any(
        isinstance(bit, bool) or not isinstance(bit, int) or bit not in (0, 1)
        for bit in result
    ):
        raise ValueError("A message can contain only 0 and 1.")
    return result
