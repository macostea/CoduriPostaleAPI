from flask_restful import Resource
from flask import request
from rozipcode import code_controller
from postal.parser import parse_address


class Search(Resource):
    def get(self):
        address = request.args.get("address")

        county = request.args.get("county")
        city = request.args.get("city")
        sector = request.args.get("sector")
        street = request.args.get("street")
        house_number = request.args.get("house_number")

        if address is not None:
            components = parse_address(address, language="ro")
            print(components)
            matched_counties = [x[0] for x in components if x[1] == "state"]
            county = matched_counties[0] if len(matched_counties) != 0 else None
            matched_cities = [x[0] for x in components if x[1] == "city"]
            city = matched_cities[0] if len(matched_cities) != 0 else None
            matched_streets = [x[0] for x in components if x[1] == "road"]
            street = matched_streets[0] if len(matched_streets) != 0 else None
            matched_sectors = [x[0] for x in components if x[1] == "city_district"]
            sector = matched_sectors[0] if len(matched_sectors) != 0 else None
            matched_house_numbers = [x[0] for x in components if x[1] == "house_number"]
            house_number = matched_house_numbers[0] if len(matched_house_numbers) != 0 else None

        return code_controller.find_by_address(county, city, sector, street, house_number)
