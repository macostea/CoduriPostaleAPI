import unittest
from rozipcode.controllers import CodeController
import os


class TestCodeControllerBucharest(unittest.TestCase):
    def setUp(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))

        self.controller = CodeController(os.path.join(current_dir, "data/bucharest_input.xlsx"))

    def test_find_by_address_exact_match(self):
        matches = self.controller.find_by_address(county="bucuresti", locality="bucuresti", sector=1, street="Mincu Ion, arh.", house_number="nr. 21-T")

        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["zip"], "011357")

    def test_find_by_address_county_only(self):
        matches = self.controller.find_by_address(county="bucuresti")

        self.assertEqual(len(matches), 9)
        self.assertEqual(matches[0]["zip"], "011357")
        self.assertEqual(matches[1]["zip"], "011359")
        self.assertEqual(matches[2]["zip"], "011421")
        self.assertEqual(matches[3]["zip"], "011422")
        self.assertEqual(matches[4]["zip"], "011423")
        self.assertEqual(matches[5]["zip"], "011424")
        self.assertEqual(matches[6]["zip"], "011425")
        self.assertEqual(matches[7]["zip"], "011426")
        self.assertEqual(matches[8]["zip"], "011427")

    def test_find_by_address_city_only(self):
        matches = self.controller.find_by_address(locality="bucuresti")

        self.assertEqual(len(matches), 9)
        self.assertEqual(matches[0]["zip"], "011357")
        self.assertEqual(matches[1]["zip"], "011359")
        self.assertEqual(matches[2]["zip"], "011421")
        self.assertEqual(matches[3]["zip"], "011422")
        self.assertEqual(matches[4]["zip"], "011423")
        self.assertEqual(matches[5]["zip"], "011424")
        self.assertEqual(matches[6]["zip"], "011425")
        self.assertEqual(matches[7]["zip"], "011426")
        self.assertEqual(matches[8]["zip"], "011427")

    def test_find_by_address_sector_only(self):
        matches = self.controller.find_by_address(sector=1)

        self.assertEqual(len(matches), 9)
        self.assertEqual(matches[0]["zip"], "011357")
        self.assertEqual(matches[1]["zip"], "011359")
        self.assertEqual(matches[2]["zip"], "011421")
        self.assertEqual(matches[3]["zip"], "011422")
        self.assertEqual(matches[4]["zip"], "011423")
        self.assertEqual(matches[5]["zip"], "011424")
        self.assertEqual(matches[6]["zip"], "011425")
        self.assertEqual(matches[7]["zip"], "011426")
        self.assertEqual(matches[8]["zip"], "011427")

    def test_find_by_address_street_only(self):
        matches = self.controller.find_by_address(street="Porumbaru Emanoil")

        self.assertEqual(len(matches), 7)
        self.assertEqual(matches[0]["zip"], "011421")
        self.assertEqual(matches[1]["zip"], "011422")
        self.assertEqual(matches[2]["zip"], "011423")
        self.assertEqual(matches[3]["zip"], "011424")
        self.assertEqual(matches[4]["zip"], "011425")
        self.assertEqual(matches[5]["zip"], "011426")
        self.assertEqual(matches[6]["zip"], "011427")

    def test_find_by_address_street_only_reverse(self):
        matches = self.controller.find_by_address(street="Emanoil Porumbaru")

        self.assertEqual(len(matches), 7)
        self.assertEqual(matches[0]["zip"], "011421")
        self.assertEqual(matches[1]["zip"], "011422")
        self.assertEqual(matches[2]["zip"], "011423")
        self.assertEqual(matches[3]["zip"], "011424")
        self.assertEqual(matches[4]["zip"], "011425")
        self.assertEqual(matches[5]["zip"], "011426")
        self.assertEqual(matches[6]["zip"], "011427")

    def test_find_by_address_house_number_only(self):
        matches = self.controller.find_by_address(house_number="nr. 21-T")

        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["zip"], "011357")

    def test_find_by_address_partial_match(self):
        matches = self.controller.find_by_address(street="emanoil", house_number="27")

        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["zip"], "011422")
