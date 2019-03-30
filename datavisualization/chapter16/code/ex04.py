#I am using Death Valley data in this exercise.
import csv
from datetime import datetime
from matplotlib import pyplot as plt

#Get dates and humidity from file
with open('death_valley_2014.csv') as f:
    reader=csv.reader(f)
    headerrow=next(reader)
    dates,humidities=[],[]
    for row in reader:
        try:
            currentdate=datetime.strptime(row[0], "%Y-%m-%d")
            humidity=int(row[8])
        except ValueError:
            print(currentdate, 'missing data')
        else:
            dates.append(currentdate)
            humidities.append(humidity)

#Plot data
fig=plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, humidities, c='red', alpha=0.5)

#Format plot
plt.title("Daily mean humidity - 2014\nDeath Valley, CA", fontsize=20)
plt.xlabel('Date', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Mean Humidity (%)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

#Display data
plt.show()


#Get dates and wind speed from file
with open('death_valley_2014.csv') as f:
    reader=csv.reader(f)
    headerrow=next(reader)
    dates,speeds=[],[]
    for row in reader:
        try:
            currentdate=datetime.strptime(row[0], "%Y-%m-%d")
            speed=int(row[16])
        except ValueError:
            print(currentdate, 'missing data')
        else:
            dates.append(currentdate)
            speeds.append(speed)

# Plot data
fig=plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, speeds, c='red', alpha=0.5)

# Format plot
plt.title("Daily mean wind speed - 2014\nDeath Valley, CA", fontsize=20)
plt.xlabel('Date', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Mean Wind Speed (mph)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

#Display data
plt.show()
