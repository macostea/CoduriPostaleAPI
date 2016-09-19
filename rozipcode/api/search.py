from flask_restful import Resource
from flask import request
from rozipcode.controllers import CodeController


class Search(Resource):
    def get(self):
        county = request.args.get("county")
        city = request.args.get("city")
        sector = request.args.get("sector")
        street = request.args.get("street")
        house_number = request.args.get("house_number")

        controller = CodeController()
        return controller.find_by_address(county, city, sector, street, house_number)
