from abc import ABC, abstractmethod
from datetime import date
from locale import atof, atoi
from typing import Callable, Generic, TypeVar

from dry.comparablefloat import ComparableFloat as Cf
from dry.strutils import fstr

_T = TypeVar("_T", bound=str | int | float | date)


class _Parameter(ABC):
    def __init__(self, caption: str):
        self.__caption = caption

    def input_value(self):
        while True:
            if self._check_have_raw_value():
                print(f"\t{self.__caption} [{self._get_default_value()}]: ", end="")
            else:
                print(f"\t{self.__caption}: ", end="")
            text = input()
            if not text and self._check_have_raw_value():
                break
            if err := self._convert_str_to_buffer(text):
                print(err)
                continue
            if self._try_set_value_from_buffer() and self._need_interrupt_if_valid():
                break
        self._do_final_actions()

    def _do_final_actions(self) -> None:
        pass

    @abstractmethod
    def _need_interrupt_if_valid(self) -> bool:
        pass

    @abstractmethod
    def _check_have_raw_value(self) -> bool:
        pass

    @abstractmethod
    def _get_default_value(self) -> str:
        pass

    @abstractmethod
    def _convert_str_to_buffer(self, text: str) -> str:
        pass

    @abstractmethod
    def _try_set_value_from_buffer(self) -> bool:
        pass


class _TypifiedParameter(_Parameter, Generic[_T]):
    def __init__(
        self,
        caption: str,
        check_isvalid: Callable[[_T], bool] | None = None,
        convert_units: Callable[[_T], _T] | None = None,
    ) -> None:
        super().__init__(caption)

        self._buffer: _T
        self.__check_isvalid = check_isvalid
        self.__convert_units = convert_units

    @abstractmethod
    def try_set_value(self, raw: _T) -> bool:
        pass

    def _check_and_convert_if_valid(self, raw: _T) -> tuple[_T, bool]:
        value = self.__convert_units(raw) if self.__convert_units else raw
        is_valid = (self.__check_isvalid is None) or self.__check_isvalid(value)
        return value, is_valid

    def _try_set_value_from_buffer(self) -> bool:
        return self.try_set_value(self._buffer)


class _TypifiedIntParameter(_TypifiedParameter[int]):
    def _convert_str_to_buffer(self, text: str) -> str:
        try:
            self._buffer = atoi(text)
        except ValueError:
            return "Ожидается целое число"
        return ""


class _TypifiedFloatParameter(_TypifiedParameter[float]):
    def _convert_str_to_buffer(self, text: str) -> str:
        try:
            self._buffer = atof(text)
        except ValueError:
            return "Ожидается число"
        return ""


class _TypifiedStrParameter(_TypifiedParameter[str]):
    def _convert_str_to_buffer(self, text: str) -> str:
        value = text.strip()
        if not value:
            return "Ожидается непустая строка"
        self._buffer = value
        return ""


class _TypifiedDateParameter(_TypifiedParameter[date]):
    def _convert_str_to_buffer(self, text: str) -> str:
        try:
            self._buffer = date.fromisoformat(text)
        except ValueError:
            return "Некорректная дата"
        return ""


class _SingleParameter(_TypifiedParameter[_T]):
    def __init__(
        self,
        caption: str,
        check_isvalid: Callable[[_T], bool] | None = None,
        convert_units: Callable[[_T], _T] | None = None,
    ) -> None:
        super().__init__(caption, check_isvalid, convert_units)

        self.__value: _T
        self.__raw_value: _T | None = None
        self.__have_raw_value = False

    def _need_interrupt_if_valid(self) -> bool:
        return True

    def try_set_value(self, raw: _T) -> bool:
        value, is_valid = self._check_and_convert_if_valid(raw)
        if is_valid:
            self.__value = value
            self.__raw_value = raw
            self.__have_raw_value = True
        return is_valid

    @property
    def value(self) -> _T:
        return self.__value

    @property
    def _raw_value(self):
        return self.__raw_value

    def _check_have_raw_value(self) -> bool:
        return self.__have_raw_value


class _ListParameter(_TypifiedParameter[_T]):
    def __init__(
        self,
        caption: str,
        check_isvalid: Callable[[_T], bool] | None = None,
        convert_units: Callable[[_T], _T] | None = None,
    ) -> None:
        super().__init__(caption, check_isvalid, convert_units)

        self.__value: list[_T] = []
        self.__raw_value: list[_T] = []
        self.__need_accumulate = True

    def _need_interrupt_if_valid(self) -> bool:
        return False

    def try_set_value(self, raw: _T) -> bool:
        value, is_valid = self._check_and_convert_if_valid(raw)
        if is_valid:
            if not self.__need_accumulate:
                self.__value.clear()
                self.__raw_value.clear()
            self.__value.append(value)
            self.__raw_value.append(raw)
            self.__need_accumulate = True
        return is_valid

    @property
    def value(self) -> tuple[_T, ...]:
        return tuple(self.__value)

    def _check_have_raw_value(self) -> bool:
        return len(self.__raw_value) > 0

    def _do_final_actions(self) -> None:
        self.__need_accumulate = False


class IntParameter(_SingleParameter[int], _TypifiedIntParameter):
    def _get_default_value(self) -> str:
        return f"{self._raw_value:n}"


class FloatParameter(_SingleParameter[float], _TypifiedFloatParameter):
    def _get_default_value(self) -> str:
        assert self._raw_value is not None
        return fstr(self._raw_value)


class StrParameter(_SingleParameter[str], _TypifiedStrParameter):
    def _get_default_value(self) -> str:
        assert self._raw_value is not None
        return self._raw_value


class DateParameter(_SingleParameter[date], _TypifiedDateParameter):
    def _get_default_value(self) -> str:
        assert self._raw_value is not None
        return self._raw_value.isoformat()


class ListFloatParameter(_ListParameter[float], _TypifiedFloatParameter):
    def _get_default_value(self) -> str:
        return ", ".join([fstr(i) for i in self.__raw_value])


def mainloop(
    calc_and_print: Callable[[], None], parameters: tuple[_Parameter, ...]
) -> None:
    try:
        while True:
            for i in parameters:
                i.input_value()
            print()
            calc_and_print()
            print()
    except KeyboardInterrupt:
        pass


def ispositive(value: int | float) -> bool:
    return Cf(value) > 0


def isnotzero(value: float) -> bool:
    return Cf(value) != 0


def isthis(condition: bool, warning: str) -> bool:
    if not condition:
        print(warning)
    return condition
