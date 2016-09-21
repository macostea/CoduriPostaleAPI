from rozipparser import CodeParser
from rozipcode.utils.string_utils import strip_accents


class CodeController:
    def __init__(self, datafile):
        self.__datafile = datafile
        self.__parser = CodeParser(datafile)
        self.__codes = self.__parser.get_codes()

    def find_by_address(self, county=None, locality=None, sector=None, street=None, house_number=None):
        matches = [x.__dict__ for x in self.__codes if (True if county is None else (county is not None and x.county is not None and strip_accents(county.lower()) in strip_accents(x.county.lower()))) and
                   (True if locality is None else (locality is not None and x.locality is not None and strip_accents(locality.lower()) in strip_accents(x.locality.lower()))) and
                   (True if sector is None else (sector is not None and x.sector is not None and str(sector).lower() in str(x.sector).lower())) and
                   (True if street is None else (street is not None and x.street is not None and
                                                 (strip_accents(street.lower()) in strip_accents(x.street.lower()) or
                                                  any(word in strip_accents(x.street.lower()) for word in strip_accents(street.lower()).split())))) and
                   # TODO: House number check does not take into consideration house number ranges
                   (True if house_number is None else (house_number is not None and x.house_number is not None and house_number.lower() in x.house_number.lower()))
                   ]

        return matches
