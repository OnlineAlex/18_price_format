import unittest

from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_work_with_int(self):
        pretty_price = format_price(10120)
        self.assertEqual(pretty_price, '10 120')

    def test_work_with_float_string(self):
        pretty_price = format_price('10124.00')
        self.assertEqual(pretty_price, '10 124')

    def test_work_with_int_string(self):
        pretty_price = format_price('13523')
        self.assertEqual(pretty_price, '13 523')

    def test_work_with_not_int_or_float(self):
        pretty_price = format_price('letters string')
        self.assertIsNone(pretty_price)

    def test_work_with_float(self):
        pretty_price = format_price(10120.550)
        self.assertEqual(pretty_price, '10 120.55')

    def test_work_with_short_number(self):
        pretty_price = format_price(5)
        self.assertEqual(pretty_price, '5')

    def test_work_with_coma_in_number(self):
        pretty_price = format_price('1235,56')
        self.assertEqual(pretty_price, '1 235.56')


if __name__ == '__main__':
    unittest.main()
