from dry.measurements import mm, to_mm

from cli import FloatParameter, ispositive, mainloop


def main() -> None:
    diam = FloatParameter('Диаметр круга, мм', ispositive, mm)
    slend = FloatParameter('Гибкость стержня', ispositive)
    slend.try_set_value(250)

    def calc_and_print() -> None:
        rodlen = slend.value * diam.value / 4
        print(f'Максимальное расстояние между опорами {to_mm(rodlen):.0f} мм')

    mainloop(calc_and_print, diam, slend)


if __name__ == '__main__':
    main()
