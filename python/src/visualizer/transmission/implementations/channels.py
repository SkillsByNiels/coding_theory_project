"""Channel implementations used in transmission simulations."""

from dataclasses import dataclass

from ..models import Bits


@dataclass(frozen=True)
class DeterministicFlipChannel:
    flip_positions: tuple[int, ...] = ()

    def transmit(self, encoded: Bits) -> Bits:
        raise NotImplementedError("Implement the deterministic bit-flip channel.")
