import unittest

from currency_converter_service import CurrencyConverterService
from exceptions import UnsupportedCurrencyException, InvalidValueException


class TestCurrencyConverterService(unittest.TestCase):
    def setUp(self) -> None:
        self.converter = CurrencyConverterService()

    def test_convert_WHEN_from_currency_is_invalid_THEN_raises_unsupported_currency_exception(self):
        with self.assertRaises(UnsupportedCurrencyException):
            self.converter.convert('LGPD', 'BRL', 1000.0)

    def test_convert_WHEN_to_currency_is_invalid_THEN_raises_unsupported_currency_exception(self):
        with self.assertRaises(UnsupportedCurrencyException):
            self.converter.convert('BRL', 'GDPR', 1000.0)

    def test_convert_WHEN_value_is_none_THEN_raises_invalid_value_exception(self):
        with self.assertRaises(InvalidValueException):
            self.converter.convert('BRL', 'EUR', None)

    def test_convert_WHEN_value_is_negative_THEN_raises_invalid_value_exception(self):
        with self.assertRaises(InvalidValueException):
            self.converter.convert('BRL', 'EUR', -100)
