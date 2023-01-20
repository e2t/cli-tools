from abc import ABC, abstractmethod
from locale import atof, atoi
from typing import Callable, Generic, TypeVar

from dry.comparablefloat import ComparableFloat as Cf

T = TypeVar('T', bound=str | int | float)


def all_valid(_: T) -> bool:
    return True


def unconverted(value: T) -> T:
    return value


def str_to_int(text: str) -> int:
    try:
        return atoi(text)
    except ValueError as exc:
        valuef = atof(text)
        if valuef.is_integer():
            return int(valuef)
        raise ValueError() from exc


class Parameter(ABC, Generic[T]):
    def __init__(self, caption: str,
                 check_isvalid: Callable[[T], bool] | None = None,
                 convert_units: Callable[[T], T] | None = None) -> None:
        self._caption = caption
        self._convert_units: Callable[[T], T] = convert_units or unconverted
        self._check_isvalid: Callable[[T], bool] = check_isvalid or all_valid
        self._type_error = 'Неправильный тип данных'
        self._break_if_valid: bool

    def input_value(self) -> None:
        while True:
            text = input(f'\t{self._caption}{self._defvalue()}: ')
            if text == '' and self._have_raw_value():
                break
            try:
                raw = self._convert_str(text)
            except ValueError:
                print(self._type_error)
                continue
            if self.try_set_value(raw) and self._break_if_valid:
                break
        self._finish_input()

    def try_set_value(self, raw: T) -> bool:
        value = self._convert_units(raw)
        res = self._check_isvalid(value)
        if res:
            self._set_values(value, raw)
        return res

    def _finish_input(self) -> None:
        pass

    @abstractmethod
    def _defvalue(self) -> str:
        pass

    @abstractmethod
    def _convert_str(self, text: str) -> T:
        pass

    @abstractmethod
    def _set_values(self, value: T, raw: T) -> None:
        pass

    @abstractmethod
    def _have_raw_value(self) -> bool:
        pass


class SingleParameter(Parameter[T]):
    def __init__(self, caption: str,
                 check_isvalid: Callable[[T], bool] | None = None,
                 convert_units: Callable[[T], T] | None = None) -> None:
        super().__init__(caption, check_isvalid, convert_units)

        self._value: T
        self._raw_value: T | None = None
        self._break_if_valid = True

    def _set_values(self, value: T, raw: T) -> None:
        self._value = value
        self._raw_value = raw

    def _have_raw_value(self) -> bool:
        return self._raw_value is not None

    @property
    def value(self) -> T:
        return self._value


class ListParameter(Parameter[T]):
    def __init__(self, caption: str,
                 check_isvalid: Callable[[T], bool] | None = None,
                 convert_units: Callable[[T], T] | None = None) -> None:
        super().__init__(caption, check_isvalid, convert_units)

        self._value: list[T] = []
        self._raw_value: list[T] = []
        self._break_if_valid = False
        self._count = 0

    def _set_values(self, value: T, raw: T) -> None:
        if not self._count:
            self._value.clear()
            self._raw_value.clear()
        self._value.append(value)
        self._raw_value.append(raw)
        self._count += 1

    def _finish_input(self) -> None:
        self._count = 0

    def _defvalue(self) -> str:
        return f' {self._raw_value}' if self._have_raw_value() else ''

    def _have_raw_value(self) -> bool:
        return bool(self._raw_value)

    @property
    def value(self) -> tuple[T, ...]:
        return tuple(self._value)


class IntParameter(SingleParameter[int]):
    def __init__(self, caption: str,
                 check_isvalid: Callable[[int], bool] | None = None,
                 convert_units: Callable[[int], int] | None = None) -> None:
        super().__init__(caption, check_isvalid, convert_units)

        self._value = 0
        self._type_error = 'Ожидается целое число'

    def _convert_str(self, text: str) -> int:
        return str_to_int(text)

    def _defvalue(self) -> str:
        return f' [{self._raw_value:n}]' if self._have_raw_value() else ''


class FloatParameter(SingleParameter[float]):
    def __init__(self, caption: str,
                 check_isvalid: Callable[[float], bool] | None = None,
                 convert_units: Callable[[float], float] | None = None
                 ) -> None:
        super().__init__(caption, check_isvalid, convert_units)

        self._value = .0
        self._type_error = 'Ожидается число'

    def _convert_str(self, text: str) -> float:
        return atof(text)

    def _defvalue(self) -> str:
        return f' [{self._raw_value:n}]' if self._have_raw_value() else ''


class StrParameter(SingleParameter[str]):
    def __init__(self, caption: str,
                 check_isvalid: Callable[[str], bool] | None = None,
                 convert_units: Callable[[str], str] | None = None) -> None:
        super().__init__(caption, check_isvalid, convert_units)

        self._value = ''

    def _convert_str(self, text: str) -> str:
        return text.strip()

    def _defvalue(self) -> str:
        return f' [{self._raw_value}]' if self._have_raw_value() else ''


class ListFloatParameter(ListParameter[float]):
    def __init__(self, caption: str,
                 check_isvalid: Callable[[float], bool] | None = None,
                 convert_units: Callable[[float], float] | None = None
                 ) -> None:
        super().__init__(caption, check_isvalid, convert_units)

        self._type_error = 'Ожидается число'

    def _convert_str(self, text: str) -> float:
        return atof(text)


def mainloop(calc_and_print: Callable[[], None],
             *parameters: Parameter[T]) -> None:
    while True:
        for i in parameters:
            i.input_value()
        print()
        calc_and_print()
        print()


def ispositive(value: int | float) -> bool:
    return Cf(value) > Cf(0)


def isnotzero(value: float) -> bool:
    return Cf(value) != Cf(0)


def isthis(condition: bool, warning: str) -> bool:
    if not condition:
        print(warning)
    return condition
