from math import pi

from dry.mathutils import STEEL_ELAST
from dry.measurements import mm

from cli import FloatParameter, ispositive, mainloop


def main() -> None:
    print("\tРасчет на потерю устойчивости\n")
    force = FloatParameter("Осевая сила, Н", ispositive)
    diam = FloatParameter("Диаметр круга, мм", ispositive, mm)
    length = FloatParameter("Длина рабочего участка, мм", ispositive, mm)
    mju = FloatParameter("Коэф. приведения длины", ispositive)
    mju.try_set_value(1)

    def calc_and_print() -> None:
        axial_moment = pi * diam.value**4 / 64
        reserve = (
            axial_moment
            / force.value
            * STEEL_ELAST
            * (pi / length.value / mju.value) ** 2
        )
        print(f"Запас прочности {reserve:.2f}")

    mainloop(calc_and_print, (force, diam, length, mju))


if __name__ == "__main__":
    main()
