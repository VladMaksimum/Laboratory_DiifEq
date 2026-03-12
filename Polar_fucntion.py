from typing import Sequence, Callable, Iterable
import numpy as np


class PolarFunction:
    def __init__(self, left: str, right: str, variables: tuple[str, str], simple_functions: dict[str, Callable],\
                r: Sequence, phi: Sequence) -> None:
        self._expr = f'{left} - ({right})'
        self._vars = variables
        self._funcs = simple_functions
        self._r = r
        self._phi = phi

    def solve_in_point(self, r: Sequence[Sequence], phi: Sequence[Sequence],parametrs: dict = {}) -> float | Iterable[Iterable]:
        var1 = self._vars[0]
        var2 = self._vars[1]

        return eval(self._expr, {}, {var1: r, var2: phi, **self._funcs, **parametrs})
    
    def solve_in_ranges(self, parametrs: dict = {}) -> Sequence[Sequence]:
        R, PHI = np.meshgrid(self._r, self._phi)

        z = self.solve_in_point(R, PHI, parametrs)
        return z