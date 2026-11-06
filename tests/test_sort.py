import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class SortCartTests(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.zebra = DigitalVideoDisc("Zebra", cost=10.0)
        self.alpha = DigitalVideoDisc("Alpha", cost=30.0)
        self.beta = DigitalVideoDisc("Beta", cost=20.0)

        for dvd in [self.zebra, self.alpha, self.beta]:
            self.cart.add_dvd(dvd)

    def test_sort_by_title(self):
        self.cart.sort_by_title()

        self.assertEqual(
            self.cart.items,
            [self.alpha, self.beta, self.zebra],
        )
        self.assertAlmostEqual(self.cart.total_cost(), 60.0)

    def test_sort_by_cost(self):
        self.cart.sort_by_cost()

        self.assertEqual(
            self.cart.items,
            [self.zebra, self.beta, self.alpha],
        )
        self.assertAlmostEqual(self.cart.total_cost(), 60.0)


if __name__ == "__main__":
    unittest.main()