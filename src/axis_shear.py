"""Модуль вычисляет максимальную силу на срез для осей разных диаметров."""
import sys
sys.path.append('..')
from dry.core import to_mm, to_mpa, to_kgf, compute_area_circle


MAX_STRESS_SHEAR = 55e6  # Допускаемое напряжение среза, Па
QTY_AXLES = 1


# TODO: Переделать в cli-приложение с вводом диаметра и напряжения среза
# (предварительно равным 55 МПа)
def main() -> None:
    # Информационный заголовок для пользователя
    print(f'Число осей: {QTY_AXLES}\n'
          f'Допустимое напряжение на срез: {to_mpa(MAX_STRESS_SHEAR):g} МПа\n')

    # Находим максимальную силу на срез для каждого диаметра
    for diameter in (10e-3, 12e-3, 16e-3, 18e-3, 20e-3, 30e-3, 40e-3):
        cross_sectional_area = compute_area_circle(diameter)
        max_force = MAX_STRESS_SHEAR * cross_sectional_area * QTY_AXLES
        print(f'{to_mm(diameter):g} мм - max {to_kgf(max_force):4.0f} кгс')


if __name__ == '__main__':
    main()
