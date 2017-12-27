"""Программа для расчета шпонок на срез."""
import sys
from typing import Tuple, NamedTuple
from cli import FloatParameter, mainloop, is_positive, is_this, from_mm
sys.path.append('..')
from dry.core import to_mm, to_mpa


# От - включительно
# До - включительно
# Свыше - НЕвключительно


class ParalKey(NamedTuple):
    max_diam: float
    width: float
    height: float
    shaft_depth: float
    sleeve_depth: float
    radius: float


# ГОСТ 23360-78
# Альтернативные типоразмеры:
#           ParalKey(0.03,  0.007, 0.007, 0.004, 0.0033, 0.00025),
#           ParalKey(0.095, 0.024, 0.014, 0.009, 0.0054, 0.0006),
STD_KEYS = (ParalKey(0.008, 0.002, 0.002, 0.0012, 0.001, 0.00016),
            ParalKey(0.01, 0.003, 0.003, 0.0018, 0.0014, 0.00016),
            ParalKey(0.012, 0.004, 0.004, 0.0025, 0.0018, 0.00016),
            ParalKey(0.017, 0.005, 0.005, 0.003, 0.0023, 0.00025),
            ParalKey(0.022, 0.006, 0.006, 0.0035, 0.0028, 0.00025),
            ParalKey(0.03, 0.008, 0.007, 0.004, 0.0033, 0.00025),
            ParalKey(0.038, 0.01, 0.008, 0.005, 0.0033, 0.0004),
            ParalKey(0.044, 0.012, 0.008, 0.005, 0.0033, 0.0004),
            ParalKey(0.05, 0.014, 0.009, 0.0055, 0.0038, 0.0004),
            ParalKey(0.058, 0.016, 0.01, 0.006, 0.0043, 0.0004),
            ParalKey(0.065, 0.018, 0.011, 0.007, 0.0044, 0.0004),
            ParalKey(0.075, 0.02, 0.012, 0.0075, 0.0049, 0.0006),
            ParalKey(0.085, 0.022, 0.014, 0.009, 0.0054, 0.0006),
            ParalKey(0.095, 0.025, 0.014, 0.009, 0.0054, 0.0006),
            ParalKey(0.11, 0.028, 0.016, 0.01, 0.0064, 0.0006),
            ParalKey(0.13, 0.032, 0.018, 0.011, 0.0074, 0.0006),
            ParalKey(0.15, 0.036, 0.02, 0.012, 0.0084, 0.001),
            ParalKey(0.17, 0.04, 0.022, 0.013, 0.0094, 0.001),
            ParalKey(0.2, 0.045, 0.025, 0.015, 0.01, 0.001),
            ParalKey(0.23, 0.05, 0.028, 0.017, 0.0114, 0.001),
            ParalKey(0.26, 0.056, 0.032, 0.02, 0.0124, 0.0016),
            ParalKey(0.29, 0.063, 0.032, 0.02, 0.0124, 0.0016),
            ParalKey(0.33, 0.07, 0.036, 0.022, 0.0144, 0.0016),
            ParalKey(0.38, 0.08, 0.04, 0.025, 0.0154, 0.0025),
            ParalKey(0.44, 0.09, 0.045, 0.028, 0.0174, 0.0025),
            ParalKey(0.5, 0.1, 0.05, 0.031, 0.0195, 0.0025))


LEN_KEYS: Tuple = (
    0.006, 0.008, 0.01, 0.012, 0.014, 0.016, 0.018, 0.02, 0.022, 0.025, 0.028,
    0.032, 0.036, 0.04, 0.045, 0.05, 0.056, 0.063, 0.07, 0.08, 0.09, 0.1, 0.11,
    0.125, 0.14, 0.16, 0.18, 0.2, 0.22, 0.25, 0.28, 0.32, 0.36, 0.4, 0.45, 0.5)


def search_key(diam: float) -> ParalKey:
    iterator = filter(lambda x: diam <= x.max_diam, STD_KEYS)
    try:
        result = next(iterator)
    except StopIteration:
        result = STD_KEYS[-1]
    return result


def work_len_by_crushing(torque: float, diam: float, key: ParalKey,
                         allow_stress_by_crushing: float) -> float:
    return torque / (0.5 * diam * (key.height - key.shaft_depth) *
                     allow_stress_by_crushing)


def work_len_by_shear(torque: float, diam: float, key: ParalKey,
                      allow_stress_by_shear: float) -> float:
    return torque / (0.5 * (diam + (key.height - key.shaft_depth)) *
                     key.width * allow_stress_by_shear)


def search_std_length(length: float) -> str:
    iterator = filter(lambda i: i > length, LEN_KEYS)
    try:
        result = f' -> {to_mm(next(iterator)):g}'
    except StopIteration:
        result = ''
    return result


def main() -> None:
    allow_stress_by_crushing = 210e6
    allow_stress_by_shear = 85e6
    print('Сталь 45, допускаемое напряжение при смятии {0:g} МПа, '
          'при срезе {1:g} МПа'.format(to_mpa(allow_stress_by_crushing),
                                       to_mpa(allow_stress_by_shear)))
    print('Переменная нагрузка: от нуля до максимума')
    print('Призматическая шпонка, исполнение 1\n')

    torque = FloatParameter('Крутящий момент, Нм', is_positive, None)

    def check_diam(val: float) -> bool:
        min_diam = 6e-3  # включительно
        max_diam = STD_KEYS[-1].max_diam  # включительно
        return is_this(
            val >= min_diam,
            'Не может быть меньше {0} мм'.format(min_diam * 1e3)) and \
            is_this(val <= max_diam,
                    'Не может быть больше {0} мм'.format(max_diam * 1e3))

    diam = FloatParameter('Диаметр, мм', check_diam, from_mm)

    def compute_and_print() -> None:
        key = search_key(diam.value)
        print('Шпонка: %gx%g, паз вала %g, паз втулки %g, радиус %g'
              % (key.width * 1e3, key.height * 1e3, key.shaft_depth * 1e3,
                 key.sleeve_depth * 1e3, key.radius * 1e3))

        work_len = max(
            work_len_by_crushing(torque.value, diam.value, key,
                                 allow_stress_by_crushing),
            work_len_by_shear(torque.value, diam.value, key,
                              allow_stress_by_shear))
        full_len = work_len + key.width
        print('Одна шпонка: рабочая длина %.1f -> полная длина %.1f%s' % (
            to_mm(work_len), to_mm(full_len), search_std_length(full_len)))

        coef = 0.75
        work_len2 = max(
            work_len_by_crushing(torque.value / 2, diam.value, key,
                                 allow_stress_by_crushing * coef),
            work_len_by_shear(torque.value / 2, diam.value, key,
                              allow_stress_by_shear * coef))
        full_len2 = work_len2 + key.width
        print('Две  шпонки: рабочая длина %.1f -> полная длина %.1f%s' % (
            to_mm(work_len2), to_mm(full_len2), search_std_length(full_len2)))

    mainloop((torque, diam), compute_and_print)


if __name__ == '__main__':
    main()
