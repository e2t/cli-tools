from dry.comparablefloat import ComparableFloat as Cf

from cli import FloatParameter, ispositive, isthis, mainloop


def main() -> None:
    print("\tВысоту щита и напор вводите в одинаковых единицах измерения.\n")
    gate = FloatParameter("Высота щита", ispositive)

    def check_head(value: float) -> bool:
        return isthis(
            Cf(value) >= gate.value, "Напор не может быть меньше высоты щита."
        )

    head = FloatParameter("Напор", check_head)

    def calc_and_print() -> None:
        discr = 4 * head.value**2 - 4 * gate.value * head.value + 2 * gate.value**2
        middle = head.value - discr**0.5 / 2
        print(f"Высота до середины: {middle:.3f}")

    mainloop(calc_and_print, (gate, head))


if __name__ == "__main__":
    main()
