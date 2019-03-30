#I am using Death Valley data in this exercise.
import csv
from datetime import datetime
from matplotlib import pyplot as plt

#Get dates, high, and low temperatures from file.
with open('death_valley_2014.csv') as f:
    reader=csv.reader(f)
    headerrow=next(reader)
    dates,highs,lows=[],[],[]
    for row in reader:
        try:
            currentdate=datetime.strptime(row[0],"%Y-%m-%d")
            high=int(row[1])
            low=int(row[3])
        except ValueError:
            print(currentdate,'missing data')
        else:
            dates.append(currentdate)
            highs.append(high)
            lows.append(low)

#Plot data
fig=plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Format plot
plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize=20)
plt.xlabel('Date', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

#Display data
plt.show()
