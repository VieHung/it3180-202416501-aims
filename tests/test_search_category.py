import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class SearchCategoryTests(unittest.TestCase):
    def test_search_by_category(self):
        lion = DigitalVideoDisc("The Lion King", category="Animation")
        star = DigitalVideoDisc("Star Wars", category="Science Fiction")
        aladdin = DigitalVideoDisc("Aladdin", category="Animation")

        result = search_by_category(
            [lion, star, aladdin],
            "Animation",
        )

        self.assertEqual(result, [lion, aladdin])


if __name__ == "__main__":
    unittest.main()