from math import pi

from cli import FloatParameter, IntParameter, ispositive, mainloop


def ratio_range(base: float, mincoef: float, maxcoef: float) -> str:
    return f'{base * mincoef:n}…{base * maxcoef:n}'


def main() -> None:
    teeth = IntParameter('Число зубьев, Z', ispositive)
    module = FloatParameter('Модуль', ispositive)

    def calc_and_print() -> None:
        pitch = module.value * pi
        ext_diam = module.value * (teeth.value + 2)
        shaft = ext_diam / 5
        print(f'Диаметр выступов зубьев = {ext_diam:n}')
        print(f'Делительный диаметр = {module.value * teeth.value:n}')
        print('Диаметр впадин зубьев = '
              f'{module.value * (teeth.value - 2.5):n}')
        print(f'Шаг зубьев = {pitch:n}')
        print(f'Высота зуба = {2.25 * module.value:n}')
        print(f'Высота головки зуба = {module.value:n}')
        print(f'Высота ножки зуба = {1.25 * module.value:n}')
        print(f'Толщина зуба = {0.5 * pitch:n}')
        print(f'Ширина впадин = {0.5 * pitch:n}')
        print(f'Ширина зуба = {ratio_range(module.value, 6, 8)}')
        print(f'Диаметр вала (ГОСТ 6636-69) = {shaft:n}')
        print(f'Диаметр ступицы = {ratio_range(shaft, 1.5, 2)}')
        print(f'Длина ступицы = {ratio_range(shaft, 1.2, 1.8)}')
        print(f'Толщина венца = {ratio_range(module.value, 2.5, 4)}')
        print(f'Толщина диска = {ratio_range(module.value, 3, 3.5)}')

    mainloop(calc_and_print, teeth, module)


if __name__ == '__main__':
    main()
