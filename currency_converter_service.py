from currency_type import CurrencyType


class CurrencyConverterService:
    def __init__(self):
        self.currency_value_to_dollar_mapper = {
            CurrencyType.DOLLAR: 1.0,
            CurrencyType.REAL: 5.0,
            CurrencyType.EURO: 0.9,
            CurrencyType.POUND: 0.74
        }

    def convert(self, from_currency: str, to_currency: str, value: float) -> float:
        pass
