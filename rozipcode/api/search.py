from flask_restful import Resource
from flask import request
from rozipcode import code_controller


class Search(Resource):
    def get(self):
        county = request.args.get("county")
        city = request.args.get("city")
        sector = request.args.get("sector")
        street = request.args.get("street")
        house_number = request.args.get("house_number")

        return code_controller.find_by_address(county, city, sector, street, house_number)
