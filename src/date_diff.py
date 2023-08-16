from datetime import date

from dry.comparablefloat import ComparableFloat as Cf
from dry.strutils import fstr

from cli import DateParameter, mainloop

_DAYS_IN_YEAR = 365.2425
_DAYS_IN_MONTH = _DAYS_IN_YEAR / 12


def main() -> None:
    date1 = DateParameter("Дата #1")
    date1.try_set_value(date.today())
    date2 = DateParameter("Дата #2")
    date2.try_set_value(date.today())

    def calc_and_print() -> None:
        days = abs((date1.value - date2.value).days)
        months = days / _DAYS_IN_MONTH
        years = days / _DAYS_IN_YEAR
        if Cf(years) > 0:
            print(f"Лет: {fstr(years,1,1)}")
        if Cf(months) > 0:
            print(f"Месяцев: {fstr(months,1,1)}")
        print(f"Дней: {fstr(days,0,0)}")

    mainloop(calc_and_print, (date1, date2))


if __name__ == "__main__":
    main()
