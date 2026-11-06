import unittest

from warehouse.quantity import parse_quantity


class QuantityTests(unittest.TestCase):
    def test_valid_quantity(self):
        self.assertEqual(parse_quantity("3"), 3)
        self.assertEqual(parse_quantity("  10  "), 10)

    def test_zero_quantity(self):
        with self.assertRaises(ValueError):
            parse_quantity("0")

    def test_negative_quantity(self):
        with self.assertRaises(ValueError):
            parse_quantity("-1")
        with self.assertRaises(ValueError):
            parse_quantity("-100")
