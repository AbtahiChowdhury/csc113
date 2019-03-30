import json
import pygal.maps
from pygal.maps.world import COUNTRIES
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

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


#Load the data into a list.
with open('gdp_data.json') as f:
    gdpdata=json.load(f)

#Build a dictionary of gross domestic product data.
gdps={}
for gdpdict in gdpdata:
    if gdpdict['Year'] == 2010:
        countryname=gdpdict['Country Name']
        gdp=int(gdpdict['Value'])
        code=getCountryCode(countryname)
        if code:
            gdps[code]=gdp

#Group the countries into 3 population levels.
gdps1,gdps2,gdps3={},{},{}
for cc,gdp in gdps.items():
    if gdp<100000000000:
        gdps1[cc]=gdp
    elif gdp<10000000000000:
        gdps2[cc]=gdp
    else:
        gdps3[cc]=gdp

#Print how many countries are in each level.
print(len(gdps1), len(gdps2), len(gdps3))

#Visualize the results
wmstyle=RS('#336699', base_style=LCS)
wm=pygal.maps.world.World(style=wmstyle)
wm.title='World Gross Domestic Product in 2010, by Country'
wm.add('0-100B', gdps1)
wm.add('100B-10T', gdps2)
wm.add('>10T', gdps3)

#Create file
wm.render_to_file('ex06.svg')
