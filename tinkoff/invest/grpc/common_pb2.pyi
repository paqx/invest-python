"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class _SecurityTradingStatus:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _SecurityTradingStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_SecurityTradingStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    SECURITY_TRADING_STATUS_UNSPECIFIED: SecurityTradingStatus.ValueType = ...  # 0
    """Торговый статус не определён"""

    SECURITY_TRADING_STATUS_NOT_AVAILABLE_FOR_TRADING: SecurityTradingStatus.ValueType = ...  # 1
    """Недоступен для торгов"""

    SECURITY_TRADING_STATUS_OPENING_PERIOD: SecurityTradingStatus.ValueType = ...  # 2
    """Период открытия торгов"""

    SECURITY_TRADING_STATUS_CLOSING_PERIOD: SecurityTradingStatus.ValueType = ...  # 3
    """Период закрытия торгов"""

    SECURITY_TRADING_STATUS_BREAK_IN_TRADING: SecurityTradingStatus.ValueType = ...  # 4
    """Перерыв в торговле"""

    SECURITY_TRADING_STATUS_NORMAL_TRADING: SecurityTradingStatus.ValueType = ...  # 5
    """Нормальная торговля"""

    SECURITY_TRADING_STATUS_CLOSING_AUCTION: SecurityTradingStatus.ValueType = ...  # 6
    """Аукцион закрытия"""

    SECURITY_TRADING_STATUS_DARK_POOL_AUCTION: SecurityTradingStatus.ValueType = ...  # 7
    """Аукцион крупных пакетов"""

    SECURITY_TRADING_STATUS_DISCRETE_AUCTION: SecurityTradingStatus.ValueType = ...  # 8
    """Дискретный аукцион"""

    SECURITY_TRADING_STATUS_OPENING_AUCTION_PERIOD: SecurityTradingStatus.ValueType = ...  # 9
    """Аукцион открытия"""

    SECURITY_TRADING_STATUS_TRADING_AT_CLOSING_AUCTION_PRICE: SecurityTradingStatus.ValueType = ...  # 10
    """Период торгов по цене аукциона закрытия"""

    SECURITY_TRADING_STATUS_SESSION_ASSIGNED: SecurityTradingStatus.ValueType = ...  # 11
    """Сессия назначена"""

    SECURITY_TRADING_STATUS_SESSION_CLOSE: SecurityTradingStatus.ValueType = ...  # 12
    """Сессия закрыта"""

    SECURITY_TRADING_STATUS_SESSION_OPEN: SecurityTradingStatus.ValueType = ...  # 13
    """Сессия открыта"""

    SECURITY_TRADING_STATUS_DEALER_NORMAL_TRADING: SecurityTradingStatus.ValueType = ...  # 14
    """Доступна торговля в режиме внутренней ликвидности брокера"""

    SECURITY_TRADING_STATUS_DEALER_BREAK_IN_TRADING: SecurityTradingStatus.ValueType = ...  # 15
    """Перерыв торговли в режиме внутренней ликвидности брокера"""

    SECURITY_TRADING_STATUS_DEALER_NOT_AVAILABLE_FOR_TRADING: SecurityTradingStatus.ValueType = ...  # 16
    """Недоступна торговля в режиме внутренней ликвидности брокера"""

class SecurityTradingStatus(_SecurityTradingStatus, metaclass=_SecurityTradingStatusEnumTypeWrapper):
    """Режим торгов инструмента"""
    pass

SECURITY_TRADING_STATUS_UNSPECIFIED: SecurityTradingStatus.ValueType = ...  # 0
"""Торговый статус не определён"""

SECURITY_TRADING_STATUS_NOT_AVAILABLE_FOR_TRADING: SecurityTradingStatus.ValueType = ...  # 1
"""Недоступен для торгов"""

SECURITY_TRADING_STATUS_OPENING_PERIOD: SecurityTradingStatus.ValueType = ...  # 2
"""Период открытия торгов"""

SECURITY_TRADING_STATUS_CLOSING_PERIOD: SecurityTradingStatus.ValueType = ...  # 3
"""Период закрытия торгов"""

SECURITY_TRADING_STATUS_BREAK_IN_TRADING: SecurityTradingStatus.ValueType = ...  # 4
"""Перерыв в торговле"""

SECURITY_TRADING_STATUS_NORMAL_TRADING: SecurityTradingStatus.ValueType = ...  # 5
"""Нормальная торговля"""

SECURITY_TRADING_STATUS_CLOSING_AUCTION: SecurityTradingStatus.ValueType = ...  # 6
"""Аукцион закрытия"""

SECURITY_TRADING_STATUS_DARK_POOL_AUCTION: SecurityTradingStatus.ValueType = ...  # 7
"""Аукцион крупных пакетов"""

SECURITY_TRADING_STATUS_DISCRETE_AUCTION: SecurityTradingStatus.ValueType = ...  # 8
"""Дискретный аукцион"""

SECURITY_TRADING_STATUS_OPENING_AUCTION_PERIOD: SecurityTradingStatus.ValueType = ...  # 9
"""Аукцион открытия"""

SECURITY_TRADING_STATUS_TRADING_AT_CLOSING_AUCTION_PRICE: SecurityTradingStatus.ValueType = ...  # 10
"""Период торгов по цене аукциона закрытия"""

SECURITY_TRADING_STATUS_SESSION_ASSIGNED: SecurityTradingStatus.ValueType = ...  # 11
"""Сессия назначена"""

SECURITY_TRADING_STATUS_SESSION_CLOSE: SecurityTradingStatus.ValueType = ...  # 12
"""Сессия закрыта"""

SECURITY_TRADING_STATUS_SESSION_OPEN: SecurityTradingStatus.ValueType = ...  # 13
"""Сессия открыта"""

SECURITY_TRADING_STATUS_DEALER_NORMAL_TRADING: SecurityTradingStatus.ValueType = ...  # 14
"""Доступна торговля в режиме внутренней ликвидности брокера"""

SECURITY_TRADING_STATUS_DEALER_BREAK_IN_TRADING: SecurityTradingStatus.ValueType = ...  # 15
"""Перерыв торговли в режиме внутренней ликвидности брокера"""

SECURITY_TRADING_STATUS_DEALER_NOT_AVAILABLE_FOR_TRADING: SecurityTradingStatus.ValueType = ...  # 16
"""Недоступна торговля в режиме внутренней ликвидности брокера"""

global___SecurityTradingStatus = SecurityTradingStatus


class MoneyValue(google.protobuf.message.Message):
    """Денежная сумма в определенной валюте"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CURRENCY_FIELD_NUMBER: builtins.int
    UNITS_FIELD_NUMBER: builtins.int
    NANO_FIELD_NUMBER: builtins.int
    currency: typing.Text = ...
    """строковый ISO-код валюты"""

    units: builtins.int = ...
    """целая часть суммы, может быть отрицательным числом"""

    nano: builtins.int = ...
    """дробная часть суммы, может быть отрицательным числом"""

    def __init__(self,
        *,
        currency : typing.Text = ...,
        units : builtins.int = ...,
        nano : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["currency",b"currency","nano",b"nano","units",b"units"]) -> None: ...
global___MoneyValue = MoneyValue

class Quotation(google.protobuf.message.Message):
    """Котировка - денежная сумма без указания валюты"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UNITS_FIELD_NUMBER: builtins.int
    NANO_FIELD_NUMBER: builtins.int
    units: builtins.int = ...
    """целая часть суммы, может быть отрицательным числом"""

    nano: builtins.int = ...
    """дробная часть суммы, может быть отрицательным числом"""

    def __init__(self,
        *,
        units : builtins.int = ...,
        nano : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["nano",b"nano","units",b"units"]) -> None: ...
global___Quotation = Quotation

class Ping(google.protobuf.message.Message):
    """Проверка активности стрима."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TIME_FIELD_NUMBER: builtins.int
    @property
    def time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Время проверки."""
        pass
    def __init__(self,
        *,
        time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["time",b"time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["time",b"time"]) -> None: ...
global___Ping = Ping
