#I am using Death Valley and Sitka data in this exercise.
import csv
from datetime import datetime
from matplotlib import pyplot as plt

#Initialize lists to store the data
dates1,highs1,lows1=[],[],[]
dates2,highs2,lows2=[],[],[]

#A function to get data from a given csv file
def getData(file, dates, highs, lows):
    """get dates, high, and low temperatures from CSV file."""
    with open(file) as f:
        reader=csv.reader(f)
        headerrow=next(reader)
        for row in reader:
            try:
                currentdate=datetime.strptime(row[0], "%Y-%m-%d")
                high=int(row[1])
                low=int(row[3])
            except ValueError:
                print(currentdate, 'missing data')
            else:
                dates.append(currentdate)
                highs.append(high)
                lows.append(low)


#Call the function to get the data from the Sitka and Death Valley files
getData('death_valley_2014.csv',dates1,highs1,lows1)
getData('sitka_weather_2014.csv',dates2,highs2,lows2)

#Plot data
fig=plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates1, highs1, c='red', alpha=0.5, label='Death Valley, CA - high')
plt.plot(dates1, lows1, c='green', alpha=0.5, label='Death Valley, CA - low')
plt.plot(dates2, highs2, c='blue', alpha=0.5, label='Sitka, AK - high')
plt.plot(dates2, lows2, c='yellow', alpha=0.5, label='Sitka, AK - low')
plt.fill_between(dates1, highs1, lows1, facecolor='red', alpha=0.1)
plt.fill_between(dates2, highs2, lows2, facecolor='blue', alpha=0.1)

# Format plot
plt.title("Daily high and low temperatures - 2014 comparison\nDeath Valley, CA and Sitka, AK", fontsize=20)
plt.xlabel('Date', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

#Set range of y axis
plt.ylim([0, 120])

#Add a legend
plt.legend()

#Display data
plt.show()
