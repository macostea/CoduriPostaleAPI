import unittest
from rozipcode.controllers import CodeController
import os


class TestCodeControllerCombined(unittest.TestCase):
    def setUp(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))

        self.controller = CodeController(os.path.join(current_dir, "data/combined_input.xlsx"))

    def test_find_by_address_county_only(self):
        matches = self.controller.find_by_address(county="Ilfov")

        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["zip"], "070000")

    def test_find_by_address_locality_only(self):
        matches = self.controller.find_by_address(locality="Giurgiu")

        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["zip"], "080303")

    def test_find_by_address_street_only(self):
        matches = self.controller.find_by_address(street="Bucureşti")

        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["zip"], "080303")

    def test_find_by_address_partial_house_number(self):
        matches = self.controller.find_by_address(house_number="2")

        self.assertEqual(len(matches), 2)
        self.assertEqual(matches[0]["zip"], "011357")
        self.assertEqual(matches[1]["zip"], "080303")
