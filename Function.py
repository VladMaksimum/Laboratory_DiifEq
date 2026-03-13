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

        
        with open("data.txt", 'w') as file:
            for i in range(1, len(self._x)-1):
                for j in range(1, len(self._y)-1):
                    if abs(self._x[i]) < 0.01:
                        file.write(f'{z[j][i-1]} {z[j][i]} {z[j][i+1]} {self._x[i]=} {self._y[j]}\n')
        

        return z


if __name__ == "__main__":
    ...