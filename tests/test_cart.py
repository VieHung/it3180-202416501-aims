import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class CartTests(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()

        for index in range(MAX_NUMBERS_ORDERED):
            dvd = DigitalVideoDisc(f"DVD {index}", cost=1.0)
            self.assertTrue(cart.add_dvd(dvd))

        extra_dvd = DigitalVideoDisc("Extra DVD", cost=1.0)

        self.assertFalse(cart.add_dvd(extra_dvd))
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED)

    def test_total_cost(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("The Lion King", cost=19.95))
        cart.add_dvd(DigitalVideoDisc("Star Wars", cost=24.95))
        cart.add_dvd(DigitalVideoDisc("Aladdin", cost=18.99))

        self.assertAlmostEqual(cart.total_cost(), 63.89)


if __name__ == "__main__":
    unittest.main()