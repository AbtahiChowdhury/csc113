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
    #If the country wasn't found, return None.
    return None


#Load the data into a list.
with open('population_data.json') as f:
    popdata=json.load(f)

#Create a dictionary of population data.
populations={}
for popdict in popdata:
    if popdict['Year'] == '2010':
        countryname=popdict['Country Name']
        population=int(float(popdict['Value']))
        code=getCountryCode(countryname)
        if code:
            populations[code]=population

#Group the countries into 3 population levels
pop1,pop2,pop3={},{},{}
for cc,pop in populations.items():
    if pop<10000000:
        pop1[cc]=pop
    elif pop<1000000000:
        pop2[cc]=pop
    else:
        pop3[cc]=pop

#Print how many countries are in each level
print(len(pop1), len(pop2), len(pop3))

#Visualize the results
wmstyle=RS('#336699', base_style=LCS)
wm=pygal.maps.world.World(style=wmstyle)
wm.title='World Population in 2010, by Country'
wm.add('0-10m', pop1)
wm.add('10m-1bn', pop2)
wm.add('>1bn', pop3)

#Create file
wm.render_to_file('ex05.svg')
