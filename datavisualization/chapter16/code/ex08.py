import pygal.maps
from pygal.maps.world import COUNTRIES
import unittest

def getCountryCode(countryname):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == countryname:
            return code
        elif countryname == "Yemen, Rep.":
            return "ye"
        elif countryname == "Venezuela, RB":
            return "ve"
        elif countryname == "West Bank and Gaza":
            return "ps"
        elif countryname == "Vietnam":
            return "vn"
        elif countryname == "Tanzania":
            return "tz"
        elif countryname == "Slovak Republic":
            return "sk"
        elif countryname == "Moldova":
            return "md"
        elif countryname == "Macedonia, FYR":
            return "mk"
        elif countryname == "Macao SAR, China":
            return "mo"
        elif countryname == "Libya":
            return "ly"
        elif countryname == "Lao PDR":
            return "la"
        elif countryname == "Kyrgyz Republic":
            return "kg"
        elif countryname == "Korea, Rep.":
            return "kr"
        elif countryname == "Korea, Dem. Rep.":
            return "kp"
        elif countryname == "Iran, Islamic Rep.":
            return "ir"
        elif countryname == "Hong Kong SAR, China":
            return "hk"
        elif countryname == "Gambia, The":
            return "gm"
        elif countryname == "Egypt, Arab Rep.":
            return "eg"
        elif countryname == "Congo, Dem. Rep.":
            return "cd"
        elif countryname == "Congo, Rep.":
            return "cg"
        elif countryname == "Bolivia":
            return "bo"
        elif countryname == "Cabo Verde":
            return "cv"
    # If the country wasn't found, return None.
    return None


class CountryCodesTestCase(unittest.TestCase):
    """Tests for 'ex08.py'."""

    def testCountryCode(self):
        """Do country codes like 'kp' work?"""
        self.assertEqual(getCountryCode('Iran, Islamic Rep.'), 'ir')


unittest.main()