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

    def test_convert_WHEN_called_with_100_reais_to_dollar_THEN_returns_20(self):
        expected = 20.00

        actual = self.converter.convert('BRL', 'USD', 100)

        self.assertEqual(expected, actual)

    def test_convert_WHEN_called_with_100_dollars_to_real_THEN_returns_500(self):
        expected = 500.00

        actual = self.converter.convert('USD', 'BRL', 100)

        self.assertEqual(expected, actual)

    def test_convert_WHEN_called_with_100_dollars_to_dollar_THEN_returns_100(self):
        expected = 100.00

        actual = self.converter.convert('USD', 'USD', 100)

        self.assertEqual(expected, actual)

    def test_convert_WHEN_called_with_100_pounds_to_euro_THEN_returns_120(self):
        expected = 120.00

        actual = self.converter.convert('GBD', 'EUR', 100)

        self.assertEqual(expected, actual)

    def test_convert_WHEN_called_with_100_pounds_to_real_THEN_returns_666_and_67(self):
        expected = 666.67

        actual = self.converter.convert('GBD', 'BRL', 100)

        self.assertEqual(expected, actual)

    def test_convert_WHEN_called_with_100_reais_to_pound_THEN_returns_15(self):
        expected = 15

        actual = self.converter.convert('BRL', 'GBD', 100)

        self.assertEqual(expected, actual)

    def test_convert_WHEN_called_with_100_pounds_to_dollar_THEN_returns_133_and_33(self):
        expected = 133.33

        actual = self.converter.convert('GBD', 'USD', 100)

        self.assertEqual(expected, actual)

    def test_convert_WHEN_called_with_100_euros_to_dollar_THEN_returns_111_and_11(self):
        expected = 111.11

        actual = self.converter.convert('EUR', 'USD', 100)

        self.assertEqual(expected, actual)

    def test_convert_WHEN_called_with_100_dollars_to_pound_THEN_returns_75(self):
        expected = 75

        actual = self.converter.convert('USD', 'GBD', 100)

        self.assertEqual(expected, actual)

    def test_convert_WHEN_called_with_100_dollars_to_euro_THEN_returns_90(self):
        expected = 90

        actual = self.converter.convert('USD', 'EUR', 100)

        self.assertEqual(expected, actual)

