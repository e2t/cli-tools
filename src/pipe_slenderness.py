from dry.measurements import mm, to_mm

from cli import FloatParameter, ispositive, mainloop


def main() -> None:
    diam = FloatParameter('Диаметр трубы, мм', ispositive, mm)
    thickness = FloatParameter('Толщина стенки, мм', ispositive, mm)
    slend = FloatParameter('Гибкость стержня', ispositive)
    slend.try_set_value(250)

    def calc_and_print() -> None:
        minor_diam = diam.value - 2 * thickness.value
        pipelen = slend.value * (diam.value**2 + minor_diam**2)**0.5 / 4
        print(f'Максимальное расстояние между опорами {to_mm(pipelen):.0f} мм')

    mainloop(calc_and_print, diam, thickness, slend)


if __name__ == '__main__':
    main()
