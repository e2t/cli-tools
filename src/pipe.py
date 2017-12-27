"""Расчет трубы на потерю устойчивости."""
from math import pi
from cli import FloatParameter, is_positive, from_mm, mainloop, is_this


ELAST = 2.1e11


def main() -> None:
    force = FloatParameter('Осевая сила, Н', is_positive)
    diam = FloatParameter('Диаметр трубы, мм', is_positive, from_mm)

    def test_thickness(val: float) -> bool:
        return (is_positive(val) and is_this(
            val < diam.value / 2,
            'Значение должно быть меньне половины диаметра'))

    thick = FloatParameter('Толщина стенки, мм', test_thickness, from_mm)
    length = FloatParameter('Длина рабочего участка, мм', is_positive,
                            from_mm)

    def compute_and_print() -> None:
        moment = pi * (diam.value - thick.value)**3 * thick.value / 8
        reserve = moment / force.value * (pi / length.value)**2 * ELAST
        print(f'Запас прочности {reserve}')

    mainloop((force, diam, thick, length), compute_and_print)


if __name__ == '__main__':
    main()
