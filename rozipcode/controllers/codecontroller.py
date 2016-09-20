from rozipparser import CodeParser


class CodeController:
    def __init__(self, datafile):
        self.__datafile = datafile
        self.__parser = CodeParser(datafile)
        self.__codes = self.__parser.get_codes()

    def find_by_address(self, county=None, locality=None, sector=None, street=None, house_number=None):
        matches = [x.__dict__ for x in self.__codes if (True if county is None else (county is not None and x.county is not None and county.lower() in x.county.lower())) and
                   (True if locality is None else (locality is not None and x.locality is not None and locality.lower() in x.locality.lower())) and
                   (True if sector is None else (sector is not None and x.sector is not None and str(sector).lower() in str(x.sector).lower())) and
                   # TODO: Street names are reverse word order in data. Make sure to check for ALL words not just partial match
                   (True if street is None else (street is not None and x.street is not None and street.lower() in x.street.lower())) and
                   # TODO: House number check does not take into consideration house number ranges
                   (True if house_number is None else (house_number is not None and x.house_number is not None and house_number.lower() in x.house_number.lower()))
                   ]

        return matches
