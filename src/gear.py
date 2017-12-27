"""Вычисляет параметры зубчатой передачи."""
from math import pi
from typing import Tuple
from cli import FloatParameter, IntParameter, is_positive, mainloop


def _diapason(from_to: Tuple[float, float], coef: float) -> str:
    return f'{coef * from_to[0]:g}..{coef * from_to[1]:g}'


def main() -> None:
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
            f'Диаметр выступов зубьев = {ext_diam:g}',
            f'Делительный диаметр = {axis_diam:g}',
            f'Диаметр впадин зубьев = {inn_diam:g}',
            f'Шаг зубьев = {pitch:g}',
            f'Высота зуба = {tooth_height:g}',
            f'Высота головки зуба = {tooth_top_height:g}',
            f'Высота ножки зуба = {tooth_bottom_height:g}',
            f'Толщина зуба = {tooth_thickness:g}',
            f'Ширина впадин = {cavity_width:g}',
            f'Ширина зуба = {tooth_width}',
            f'Диаметр вала (ГОСТ 6636-69) = {shaft_diam:g}',
            f'Диаметр ступицы = {hub_diam}',
            f'Длина ступицы = {hub_length}',
            f'Толщина венца = {face_width}',
            f'Толщина диска = {disk_width}',
            sep='\n')

    mainloop((teeth_number, module), compute_and_print)


if __name__ == '__main__':
    main()
