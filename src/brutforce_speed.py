import math

from dry.comparablefloat import ComparableFloat as Cf

from cli import IntParameter, ispositive, mainloop

_UNITS = {
    60 * 60 * 24 * 365: "year",
    60 * 60 * 24 * 30: "month",
    60 * 60 * 24: "day",
    60 * 60: "hour",
    60: "minute",
    1: "second",
}


def _time_to_str(time: float) -> str:
    for volume, name in _UNITS.items():
        if Cf(time) >= volume:
            break
    else:
        return "less than a " + list(_UNITS.values())[-1]
    count = time / volume
    end = "s" if Cf(count) > 1 else ""
    return f"{count:7.0f} {name}{end}"


def main() -> None:
    speed = IntParameter("Brut-force speed, paswd/sec", ispositive)
    speed.try_set_value(1_000_000)

    def calc_and_print() -> None:
        symbol_count = 36
        for i in range(1, 14):
            variant_count = symbol_count**i
            time = variant_count / speed.value
            stime = _time_to_str(time)
            entropy = math.log2(variant_count)
            print(
                f"{i:2d} symb. {variant_count:21.0f} variants, "
                f"{entropy:2.0f} bits, {stime}"
            )

    mainloop(calc_and_print, (speed,))


if __name__ == "__main__":
    main()
