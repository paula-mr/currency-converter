from currency_type import CurrencyType
from exceptions import UnsupportedCurrencyException, InvalidValueException


class CurrencyConverterService:
    def __init__(self):
        self.currency_value_to_dollar_mapper = {
            CurrencyType.DOLLAR: 1.0,
            CurrencyType.REAL: 5.0,
            CurrencyType.EURO: 0.9,
            CurrencyType.POUND: 0.75
        }

    def convert(self, from_currency: str, to_currency: str, value: float) -> float:
        from_currency_type = self.__parse_currency(from_currency)
        to_currency_type = self.__parse_currency(to_currency)
        if not value or value < 0:
            raise InvalidValueException

        value_in_dollar = value / self.currency_value_to_dollar_mapper[from_currency_type]
        value_in_target_currency = value_in_dollar * self.currency_value_to_dollar_mapper[to_currency_type]
        return round(value_in_target_currency, 2)

    @classmethod
    def __parse_currency(cls, currency: str):
        try:
            return CurrencyType(currency)
        except ValueError:
            raise UnsupportedCurrencyException
