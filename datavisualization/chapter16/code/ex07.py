import csv
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

# Load the data into a list.
with open('API_EN.POP.DNST_DS2_en_csv_v2(modified).csv') as f:
    reader=csv.reader(f)
    headerrow=next(reader)
    # Build a dictionary of population density data.
    densities={}
    for row in reader:
        try:
            countryname=row[0]
            density=float(row[-3])
            code=getCountryCode(countryname)
        except ValueError:
            print('Missing data for '+countryname)
        else:
            if code:
                densities[code]=density

# Group the countries into 3 population levels.
densities1,densities2,densities3={},{},{}
for cc,density in densities.items():
    if density<10:
        densities1[cc]=density
    elif density<100:
        densities2[cc]=density
    else:
        densities3[cc]=density

# See how many countries are in each level.
print(len(densities1), len(densities2), len(densities3))

#Visualize the results
wmstyle=RS('#336699', base_style=LCS)
wm=pygal.maps.world.World(style=wmstyle)
wm.title='World density in 2016, by Country'
wm.add('0-9 ppl/sq.km', densities1)
wm.add('10-99 ppl/sq.km', densities2)
wm.add('>100 ppl/sq.km', densities3)

#Create file
wm.render_to_file('ex07.svg')
