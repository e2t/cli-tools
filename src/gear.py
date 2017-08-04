"""Вычисляет параметры зубчатой передачи."""
from math import pi
from typing import Tuple
from cli import FloatParameter, IntParameter, is_positive, mainloop


def _diapason(from_to: Tuple[float, float], coef: float) -> str:
    return '%g..%g' % (coef * from_to[0], coef * from_to[1])


def main() -> None:
    """Выполняется при запуске модуля."""
    teeth_number = IntParameter('Число зубьев, Z', is_positive)
    module = FloatParameter('Модуль', is_positive)

    def compute_and_print() -> None:
        tooth_height = 2.25 * module.value
        tooth_top_height = module.value
        tooth_bottom_height = 1.25 * module.value
        axis_diam = module.value * teeth_number.value
        ext_diam = module.value * (teeth_number.value + 2)
        inn_diam = module.value * (teeth_number.value - 2.5)
        pitch = module.value * pi
        tooth_thickness = 0.5 * pitch
        cavity_width = 0.5 * pitch
        shaft_diam = ext_diam / 5
        hub_diam = _diapason((1.5, 2), shaft_diam)
        hub_length = _diapason((1.2, 1.8), shaft_diam)
        tooth_width = _diapason((6, 8), module.value)
        face_width = _diapason((2.5, 4), module.value)
        disk_width = _diapason((3, 3.5), module.value)
        print(
            'Диаметр выступов зубьев = %g' % ext_diam,
            'Делительный диаметр = %g' % axis_diam,
            'Диаметр впадин зубьев = %g' % inn_diam,
            'Шаг зубьев = %g' % pitch,
            'Высота зуба = %g' % tooth_height,
            'Высота головки зуба = %g' % tooth_top_height,
            'Высота ножки зуба = %g' % tooth_bottom_height,
            'Толщина зуба = %g' % tooth_thickness,
            'Ширина впадин = %g' % cavity_width,
            'Ширина зуба = %s' % tooth_width,
            'Диаметр вала (ГОСТ 6636-69) = %g' % shaft_diam,
            'Диаметр ступицы = %s' % hub_diam,
            'Длина ступицы = %s' % hub_length,
            'Толщина венца = %s' % face_width,
            'Толщина диска = %s' % disk_width,
            sep='\n')

    mainloop((teeth_number, module), compute_and_print)


if __name__ == '__main__':
    main()
