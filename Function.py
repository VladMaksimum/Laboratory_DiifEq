from typing import Callable, Iterable, Sequence, Optional
import numpy as np

Numeric = int | float

class Function:
    def __init__(self, left: str, right: str, variables: tuple[str, str], simple_functions: dict[str, Callable]) -> None:
        self._expr = f'{left} - {right}'
        self._vars = variables
        self._funcs = simple_functions

    def solve_in_point(self, x: float | Iterable[Iterable], y: float | Iterable[Iterable]) -> float | Iterable[Iterable]:
        var1 = self._vars[0]
        var2 = self._vars[1]

        return eval(self._expr, {}, {var1: x, var2: y, **self._funcs})
    
    def solve_in_ranges(self, ranges: Sequence[Sequence], delta: float) -> Sequence[Sequence]:
        X, Y = np.meshgrid(ranges[0], ranges[1])

        z = self.solve_in_point(X, Y)

        with open("data.txt", 'w') as file:
            for i in range(len(ranges[0])):
                for j in range(len(ranges[1])):
                    if abs(z[j][i]) < delta and abs(ranges[0][i]) < 0.25 and abs(ranges[1][j]) < 0.25:
                        file.write(f'{ranges[0][i]} {ranges[1][j]} {z[j][i]}\n')

        return z


if __name__ == "__main__":
    ...