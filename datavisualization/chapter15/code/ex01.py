import matplotlib.pyplot as plt

#Plot of the first 5 cudes

#Create list for x axis
xval = list(range(1, 6))
#Create list for y axis
yval = [x**3 for x in xval]

#Create scatter plot of x and y values
plt.scatter(xval, yval, s=40)

#Create labels for title, x-axis, and y-axis
plt.title("Cube Numbers")
plt.xlabel("Value")
plt.ylabel("Cube of Value")

#Create tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

#Display graph
plt.show()

#plot of the first 5000 cubic numbers

#Create list for x axis
xval = list(range(1, 5001))
#Create list for y axis
yval = [x**3 for x in xval]

#Create scatter plot of x and y values
plt.scatter(xval, yval, s=40)

#Create labels for title, x-axis, and y-axis
plt.title("Cube Numbers")
plt.xlabel("Value")
plt.ylabel("Cube of Value")

#Create tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

#Set axis range of graph
plt.axis([-1000, 6000, -20000000000, 140000000000])

#Display graph
plt.show()
