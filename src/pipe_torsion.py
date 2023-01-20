from math import pi

from dry.measurements import mm, to_mpa

from cli import FloatParameter, ispositive, mainloop


def ring_torsion_resistance_moment(major_diam: float, minor_diam: float
                                   ) -> float:
    a = minor_diam / major_diam
    return pi * major_diam**3 / 16 * (1 - a**4)


def main() -> None:
    torque = FloatParameter('Крутящий момент, Нм', ispositive)
    diam = FloatParameter('Диаметр трубы, мм', ispositive, mm)
    thickness = FloatParameter('Толщина стенки, мм', ispositive, mm)

    def calc_and_print() -> None:
        minor_diam = diam.value - 2 * thickness.value
        torsion_resistance_moment = ring_torsion_resistance_moment(
            diam.value, minor_diam)
        stress = torque.value / torsion_resistance_moment
        print(f'Напряжение {to_mpa(stress):.1f} МПа')

    mainloop(calc_and_print, torque, diam, thickness)


if __name__ == '__main__':
    main()
