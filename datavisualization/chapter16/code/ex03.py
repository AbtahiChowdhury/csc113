#I am using Death Valley data in this exercise.
import csv
from datetime import datetime
from matplotlib import pyplot as plt

#Get dates and precipitation from file.
with open('death_valley_2014.csv') as f:
    reader=csv.reader(f)
    headerrow=next(reader)
    dates,precipitations=[],[]
    for row in reader:
        try:
            currentdate=datetime.strptime(row[0], "%Y-%m-%d")
            precipitation=float(row[19])
        except ValueError:
            print(currentdate,'missing data')
        else:
            dates.append(currentdate)
            precipitations.append(precipitation)

#Plot data
fig=plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, precipitations, c='red', alpha=0.5)

#Format plot
plt.title("Daily precipitation - 2014\nDeath Valley, CA", fontsize=20)
plt.xlabel('Date', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall (inches)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

#Display data
plt.show()
