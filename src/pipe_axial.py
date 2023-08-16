from math import pi

from dry.mathutils import STEEL_ELAST
from dry.measurements import mm

from cli import FloatParameter, ispositive, mainloop


def main() -> None:
    force = FloatParameter("Осевая сила, Н", ispositive)
    diam = FloatParameter("Диаметр трубы, мм", ispositive, mm)
    thickness = FloatParameter("Толщина стенки, мм", ispositive, mm)
    length = FloatParameter("Длина рабочего участка, мм", ispositive, mm)
    mju = FloatParameter("Коэф. приведения длины", ispositive)
    mju.try_set_value(1)

    def calc_and_print() -> None:
        minor_diam = diam.value - 2 * thickness.value
        axial_moment = pi * (diam.value**4 - minor_diam**4) / 64
        reserve = (
            axial_moment
            / force.value
            * STEEL_ELAST
            * (pi / length.value / mju.value) ** 2
        )
        print(f"Запас прочности {reserve:.2f}")

    mainloop(calc_and_print, (force, diam, thickness, length, mju))


if __name__ == "__main__":
    main()
