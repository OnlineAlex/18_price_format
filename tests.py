import unittest

from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_price_int(self):
        pretty_price = format_price(10120)
        self.assertEqual(pretty_price, '10 120')

    def test_price_float_string(self):
        pretty_price = format_price('10124.00')
        self.assertEqual(pretty_price, '10 124')

    def test_price_int_string(self):
        pretty_price = format_price('13523')
        self.assertEqual(pretty_price, '13 523')

    def test_price_set(self):
        pretty_price_set = format_price({1300.5, '4000'})
        self.assertIsNone(pretty_price_set)

    def test_price_letters(self):
        pretty_price_letters = format_price('letters string')
        self.assertIsNone(pretty_price_letters)

    def test_price_list(self):
        pretty_price_list = format_price([1300.5, '4000'])
        self.assertIsNone(pretty_price_list)

    def test_price_dict(self):
        pretty_price_dict = format_price({'price': 80700})
        self.assertIsNone(pretty_price_dict)

    def test_price_tuple(self):
        pretty_price_tuple = format_price((1300.5, '4000'))
        self.assertIsNone(pretty_price_tuple)

    def test_price_bool(self):
        pretty_price_bool = format_price(False)
        self.assertIsNone(pretty_price_bool)

    def test_price_float(self):
        pretty_price = format_price(10120.550)
        self.assertEqual(pretty_price, '10 120.55')

    def test_price_short_number(self):
        pretty_price = format_price(5)
        self.assertEqual(pretty_price, '5')

    def test_price_with_coma_in_number(self):
        pretty_price = format_price('1235,56')
        self.assertIsNone(pretty_price)


if __name__ == '__main__':
    unittest.main()
