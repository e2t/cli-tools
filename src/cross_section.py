from math import pi

from dry.comparablefloat import ComparableFloat as Cf
from dry.measurements import mm, mpa, to_mm, to_mpa

from cli import FloatParameter, IntParameter, ispositive, mainloop

LIMIT_SHEAR_STRESS_AISI304 = 60e6


METRIC: dict[str, float] = {
    'М6': mm(4.918),
    'М8': mm(6.647),
    'М10': mm(8.376),
    'М12': mm(10.106),
    'М16': mm(13.835),
    'М20': mm(17.294)
}


def search_bolt(diam: float) -> str:
    for name, minor_diam in METRIC.items():
        if Cf(diam) <= Cf(minor_diam):
            return name
    return f'свыше {list(METRIC)[-1]}'


def main() -> None:
    count = IntParameter('Мест среза (2 для сквозных)', ispositive)
    count.try_set_value(2)
    force = FloatParameter('Нагрузка на срез, Н', ispositive)
    maxstress = FloatParameter('Допустимое напряжение, МПа', ispositive, mpa)
    maxstress.try_set_value(to_mpa(LIMIT_SHEAR_STRESS_AISI304))

    def calc_and_print() -> None:
        minarea = force.value / maxstress.value / count.value
        mindiam = (4 * minarea / pi)**0.5
        bolt = search_bolt(mindiam)
        print(f'Минимальный диаметр {to_mm(mindiam):.3f} мм, {bolt}')

    mainloop(calc_and_print, count, force, maxstress)


if __name__ == '__main__':
    main()
