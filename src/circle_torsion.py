from math import pi

from dry.measurements import mm, to_mpa

from cli import FloatParameter, ispositive, mainloop


def main() -> None:
    torque = FloatParameter('Крутящий момент, Нм', ispositive)
    diam = FloatParameter('Диаметр круга, мм', ispositive, mm)

    def calc_and_print() -> None:
        torsion_resistance_moment = pi * diam.value**3 / 16
        stress = torque.value / torsion_resistance_moment
        print(f'Наприяжение {to_mpa(stress):.1f} МПа')

    mainloop(calc_and_print, torque, diam)


if __name__ == '__main__':
    main()
