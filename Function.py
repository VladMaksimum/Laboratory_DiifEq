from typing import Callable, Iterable, Sequence, Optional
import numpy as np

Numeric = int | float

class Function:
    def __init__(self, left: str, right: str, variables: tuple[str, str], simple_functions: dict[str, Callable],\
                 x: Sequence, y: Sequence) -> None:
        self._expr = f'{left} - ({right})'
        self._vars = variables
        self._funcs = simple_functions
        self._x = x
        self._y = y

    def solve_in_point(self, x: Sequence[Sequence], y: Sequence[Sequence],parametrs: dict = {}) -> float | Iterable[Iterable]:
        var1 = self._vars[0]
        var2 = self._vars[1]

        return eval(self._expr, {}, {var1: x, var2: y, **self._funcs, **parametrs})
    
    def solve_in_ranges(self, parametrs: dict = {}) -> Sequence[Sequence]:
        X, Y = np.meshgrid(self._x, self._y)

        z = self.solve_in_point(X, Y, parametrs)

        '''
        with open("data.txt", 'w') as file:
            for i in range(len(self._x)):
                for j in range(len(self._y)):
                    if abs(z[j][i]) < delta and abs(self._x[i]) < 0.25 and abs(self._y[j]) < 0.25:
                        file.write(f'{self._x[i]} {self._x[j]} {z[j][i]}\n')
        '''

        return z


if __name__ == "__main__":
    ...