import numpy as np

Numeric = int | float
def ln(x: Numeric) -> Numeric:
    return np.log1p(x - 1)


funcs ={
    'arctg' : np.atan,
    'arccos' :np.acos,
    'arcsin' : np.asin,
    'sqrt' : np.sqrt,
    'sin' : np.sin,
    'cos' : np.cos,
    'tg' : np.tan,
    'ln' : ln,
    'exp' : np.exp,
    'pi' : np.pi
}