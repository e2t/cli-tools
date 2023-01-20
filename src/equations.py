from sympy import Symbol
from sympy.solvers import solveset

from cli import FloatParameter, mainloop


def main() -> None:
    print('\tAx^3 + Bx^2 + Cx + D = 0\n')
    a = FloatParameter('A')
    b = FloatParameter('B')
    c = FloatParameter('C')
    d = FloatParameter('D')

    def calc_and_print() -> None:
        x = Symbol('x')
        roots = solveset(a.value * x**3 + b.value * x**2
                         + c.value * x + d.value, x)
        for i, value in enumerate(roots):
            print(f'x{i + 1} = {value}')
    mainloop(calc_and_print, a, b, c, d)


if __name__ == '__main__':
    main()
