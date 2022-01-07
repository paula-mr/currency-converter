import unittest

from currency_converter_service import CurrencyConverterService


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.converter = CurrencyConverterService()

    def test_something(self):
        self.assertEqual(True, False)
