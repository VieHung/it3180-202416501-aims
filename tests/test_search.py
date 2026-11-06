import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class SearchTitleTests(unittest.TestCase):
    def test_search_by_title_is_case_insensitive(self):
        lion = DigitalVideoDisc("The Lion King")
        star = DigitalVideoDisc("Star Wars")

        result = search_by_title([lion, star], "lion")

        self.assertEqual(result, [lion])


if __name__ == "__main__":
    unittest.main()