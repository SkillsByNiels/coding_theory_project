"""Channel implementations used in transmission simulations."""

from dataclasses import dataclass

from ..models import Bits


@dataclass(frozen=True)
class DeterministicFlipChannel:
    flip_positions: tuple[int, ...] = ()

    def transmit(self, encoded: Bits) -> Bits:
        if len(encoded) != len(self.flip_positions):
            raise ValueError(
                f"Encoded message length {len(encoded)} does not match flip positions length {len(self.flip_positions)}."
            )
        return tuple(map(lambda x, y: (x + y) % 2, encoded, self.flip_positions))
