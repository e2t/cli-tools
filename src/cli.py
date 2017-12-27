"""
Модуль позволяет создавать цикличные консольные приложения.

 * Задается набор параметров, которые необходимы для решения задачи и вводятся
пользователем с клавиатуры.
 * Для каждого параметра описывается допустимый диапазон значений и своё
преобразование единиц.
 * Приглашение к вводу каждого параметра продолжается до тех пор, пока
пользователь не введет приемлемое значение.
 * После правильного ввода всех параметров запускается вычисление, результаты
выводятся на экран, затем начинается новый цикл.
 * Значения параметров, введенные пользователем в предыдущем цикле, сохраняются
и при новом вводе могут быть вызваны нажатием Enter.
"""
import sys
from typing import Callable, Tuple, Optional, Generic, TypeVar, List
from abc import abstractmethod


class EmptyLine(Exception):
    """Исключение, если пользователь ничего не ввел и нажал Enter."""

    pass


class IncorrectLine(Exception):
    """Исключение, если пользователь ввел строку, не ковертируемую в число."""

    pass


class NotAllowableValue(Exception):
    """Исключение, если пользователь ввел число, не допустимое по условию."""

    pass


def print_error(text: str) -> None:
    """Печатает сообщение об ошибке в поток ошибок."""
    print(text, file=sys.stderr)


def input_line(prompt: str) -> str:
    """
    Возвращает строку, введенную пользователем с клавиатуры.

    Выводит на экран приглашение, ожидает ввод с клавиатуры, возращает
    введенную строку. Ctrl+C завершает программу, подавляя ошибки.
    """
    try:
        return input(prompt)
    except KeyboardInterrupt:
        exit(0)


def str_to_int(text: str) -> int:
    """Преобразует строку в целое число."""
    if text:
        try:
            return int(text)
        except ValueError:
            raise IncorrectLine('Ожидается целое число')
    else:
        raise EmptyLine


def str_to_float(text: str) -> float:
    """Преобразует строку в вещественное число."""
    if text:
        try:
            return float(text)
        except ValueError:
            raise IncorrectLine('Ожидается число')
    else:
        raise EmptyLine


def is_this(condition: bool, warning: str) -> bool:
    """
    Возвращает результат проверки условия.

    Если условие ложно, печатает сообщение об ошибке.
    """
    if not condition:
        print_error(warning)
    return condition


NumberType = TypeVar('NumberType', int, float)


def is_positive(number: NumberType) -> bool:
    """Проверяет, является ли число больше нуля."""
    return is_this(number > 0, 'Число должно быть больше нуля')


def is_positive_or_zero(number: NumberType) -> bool:
    """Проверяет, является ли число больше или равным нулю."""
    return is_this(number >= 0, 'Число не должно быть меньше нуля')


def dont_convert(value: NumberType) -> NumberType:
    """Заглушка для величин, не нуждающихся в преобразовании единиц."""
    return value


def from_mm(millimeters: float) -> float:
    """Милиметры -> СИ."""
    return millimeters / 1e3


def from_l(litres: float) -> float:
    """Литры -> СИ."""
    return litres / 1e3


def always_allowable(_: NumberType) -> bool:
    """Заглушка для величин, не имеющих ограничений по диапазону значений."""
    return True


class Parameter(Generic[NumberType]):
    def __init__(
            self, caption: str,
            is_allowable: Optional[Callable[[NumberType], bool]]=None,
            convert_units: Optional[Callable[[NumberType], NumberType]]=None) \
            -> None:
        self.caption: str = caption
        self.is_allowable: Callable[[NumberType], bool] = always_allowable
        if is_allowable is not None:
            self.is_allowable = is_allowable
        self.convert_units: Callable[[NumberType], NumberType] = dont_convert
        if convert_units is not None:
            self.convert_units = convert_units

    def convert_and_check_value(self, raw_value: NumberType) -> NumberType:
        value = self.convert_units(raw_value)
        if not self.is_allowable(value):
            raise NotAllowableValue
        return value

    @staticmethod
    @abstractmethod
    def str_to_number(text: str) -> NumberType:
        pass

    @abstractmethod
    def input_value(self) -> None:
        """Ввод параметра, продолжается до получения приемлемого значения."""
        pass


class NumericParameter(Generic[NumberType], Parameter):
    def __init__(
            self, caption: str,
            is_allowable: Optional[Callable[[NumberType], bool]]=None,
            convert_units: Optional[Callable[[NumberType], NumberType]]=None,
            init_value: Optional[NumberType]=None) \
            -> None:
        self.prev_raw_value: Optional[NumberType] = None
        super().__init__(caption, is_allowable, convert_units)
        if init_value is not None:
            try:
                self.check_and_set(init_value)
            except NotAllowableValue:
                pass

    def input_value(self) -> None:
        while True:
            inputed_text = input_line(self.prompt())
            try:
                raw_value = self.str_to_number(inputed_text)
                try:
                    self.check_and_set(raw_value)
                    break
                except NotAllowableValue:
                    pass
            except EmptyLine as excp:
                if self.prev_raw_value is not None:
                    break
                print_error(str(excp))
            except IncorrectLine as excp:
                print_error(str(excp))

    def check_and_set(self, raw_value: NumberType) -> None:
        value = self.convert_and_check_value(raw_value)
        self._value: NumberType = value
        self.prev_raw_value = raw_value

    @property
    def value(self) -> NumberType:
        """Вовзращает значение параметра."""
        return self._value

    def prompt(self) -> str:
        if self.prev_raw_value is not None:
            # TODO: :g сокращает целое 1000000 в 1е+6
            result = '\t{0} [{1:g}]: '.format(self.caption,
                                              self.prev_raw_value)
        else:
            result = '\t{0}: '.format(self.caption)
        return result


class IntParameter(NumericParameter[int]):
    """Класс целочисленных параметров."""

    @staticmethod
    def str_to_number(text: str) -> int:
        return str_to_int(text)


class FloatParameter(NumericParameter[float]):
    """Класс вещественных параметров."""

    @staticmethod
    def str_to_number(text: str) -> float:
        return str_to_float(text)


class ArrayParameter(Generic[NumberType], Parameter):
    def __init__(
            self, caption: str,
            is_allowable: Optional[Callable[[NumberType], bool]]=None,
            convert_units: Optional[Callable[[NumberType], NumberType]]=None) \
            -> None:
        self._value: List[NumberType] = []
        super().__init__(caption, is_allowable, convert_units)

    @property
    def value(self) -> List[NumberType]:
        """Возвращает список значений параметра."""
        return self._value

    def input_value(self) -> None:
        self._value.clear()
        while True:
            inputed_text = input_line(self.prompt())
            try:
                raw_value = self.str_to_number(inputed_text)
                try:
                    self.check_and_set(raw_value)
                except NotAllowableValue:
                    pass
            except EmptyLine as excp:
                if self._value:
                    break
                print_error(str(excp))
            except IncorrectLine as excp:
                print_error(str(excp))

    def check_and_set(self, raw_value: NumberType) -> None:
        value = self.convert_and_check_value(raw_value)
        self._value.append(value)

    def prompt(self) -> str:
        return '\t{0}: '.format(self.caption)


class ArrayFloatParameter(ArrayParameter[float]):
    """Класс параметр-массива вещественных чисел."""

    @staticmethod
    def str_to_number(text: str) -> float:
        return str_to_float(text)


def mainloop(params: Tuple[Parameter, ...],
             compute_and_print: Callable[[], None]) -> None:
    """Основной цикл ввода параметров и вывода результатов."""
    while True:
        for i in params:
            i.input_value()
        print()
        compute_and_print()
        print()
