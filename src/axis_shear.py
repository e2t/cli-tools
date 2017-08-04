"""Модуль вычисляет максимальную силу на срез для осей разных диаметров."""
import sys
sys.path.append('..')
from dry.core import to_mm, to_mpa, to_kgf, compute_area_circle


# Допускаемое напряжение среза, Па
MAX_STRESS_SHEAR = 55e6


# TODO: Переделать в cli-приложение с вводом диаметра и напряжения среза
# (предварительно равным 55 МПа)
def main() -> None:
    """Выполняется при запуске модуля."""
    qty_axles = 1

    # Информационный заголовок для пользователя
    print('Число осей: {0}\nДопустимое напряжение на срез: {1:g} МПа\n'.format(
        qty_axles, to_mpa(MAX_STRESS_SHEAR)))

    # Находим максимальную силу на срез для каждого диаметра
    for diameter in [10e-3, 12e-3, 16e-3, 18e-3, 20e-3, 30e-3, 40e-3]:
        cross_sectional_area = compute_area_circle(diameter)
        max_force = MAX_STRESS_SHEAR * cross_sectional_area * qty_axles
        print('{0:g} мм - max {1:4.0f} кгс'.format(
            to_mm(diameter), to_kgf(max_force)))


if __name__ == '__main__':
    main()
