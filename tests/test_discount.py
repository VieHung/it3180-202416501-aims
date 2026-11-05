
import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class DiscountTests(unittest.TestCase):
    def test_discount_returns_remaining_total(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Sample DVD", cost=100.0))

        self.assertAlmostEqual(
            cart.total_cost_with_discount(20),
            80.0,
        )

    def test_invalid_discount_raises_value_error(self):
        cart = Cart()

        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)


if __name__ == "__main__":
    unittest.main()