from rozipparser import CodeParser
import os

codes = []


class CodeController:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.__parser = CodeParser(os.path.join(current_dir, "../data/infocod-cu-siruta-mai-2016.xlsx"))
        global codes

        if len(codes) == 0:
            codes = self.__parser.get_codes()

    def find_by_address(self, county, locality, sector, street, house_number):
        matches = [x.__dict__ for x in codes if (True if county is None else (county is not None and x.county is not None and county.lower() in x.county.lower())) and
                   (True if locality is None else (locality is not None and x.locality is not None and locality.lower() in x.locality.lower())) and
                   (True if sector is None else (sector is not None and x.sector is not None and str(sector).lower() in str(x.sector).lower())) and
                   (True if street is None else (street is not None and x.street is not None and street.lower() in x.street.lower())) and
                   (True if house_number is None else (house_number is not None and x.house_number is not None and house_number.lower() in x.house_number.lower()))
                   ]

        return matches
