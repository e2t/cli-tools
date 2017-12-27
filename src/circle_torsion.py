"""Модуль вычисляет напряжение при кручении вала или трубы."""
from math import pi
from cli import mainloop, FloatParameter, is_positive, is_positive_or_zero, \
    from_mm, is_this


def main() -> None:
    torque = FloatParameter('Крутящий момент, Нм', is_positive)
    ext_diam = FloatParameter('Наружный диаметр, мм', is_positive, from_mm)

    def check_inn_diam(val: float) -> bool:
        return is_positive_or_zero(val) and is_this(
            val < ext_diam.value, 'Не может быть меньше наружного диаметра')

    inn_diam = FloatParameter('Внутренний диаметр, мм (0 для вала)',
                              check_inn_diam, from_mm)

    def compute_and_print() -> None:
        alpha = inn_diam.value / ext_diam.value
        polar_moment = pi * ext_diam.value**3 / 16 * (1 - alpha**4)
        stress = torque.value / polar_moment
        print(f'Напряжение {stress / 1e6:.1f} МПа')

    mainloop((torque, ext_diam, inn_diam), compute_and_print)


if __name__ == '__main__':
    main()
