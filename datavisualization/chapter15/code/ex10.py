import matplotlib.pyplot as plt
import pygal
from random import randint
from random import choice

class RandomWalk():
    """A class to generate random walks."""

    def __init__(self, numofpoints=5000):
        """Initialize attributes of a walk."""
        self.numofpoints = numofpoints
        #All walks start at (0,0).
        self.xval = [0]
        self.yval = [0]

    def getStep(self):
        """Determine the direction and distance of each step."""
        direction = choice([1, -1])
        distance = choice(list(range(0, 9)))
        return direction * distance

    def fillWalk(self):
        """Calculate all the points in the walk."""

        #Keep taking steps until the walk reaches the desired length.
        while len(self.xval) < self.numofpoints:

            #Decide which direction to go and how far to go in that direction.
            xstep = self.getStep()
            ystep = self.getStep()

            #Reject moves that go nowhere.
            if xstep == 0 and ystep == 0:
                continue

            #Calculate the next x and y values.
            nextx = self.xval[-1] + xstep
            nexty = self.yval[-1] + ystep
            self.xval.append(nextx)
            self.yval.append(nexty)

class Die():
    """A class representing a single die."""

    def __init__(self, numsides=6):
        """Assume a six-sided die."""
        self.numsides=numsides

    def roll(self):
        """"Return a random value between 1 and number of sides."""
        return randint(1, self.numsides)

#Create one six side die.
die=Die()

xval=list(range(1, 51))

#Make some rolls, and store results in a list.
yval=[die.roll() for num in range(50)]

#Set size of plotting window.
plt.figure(figsize=(10, 6))

#Plot points on graph
plt.plot(xval,yval,linewidth=1)

#Set chart title and label axes.
plt.title("D6 roll results", fontsize=24)
plt.xlabel("Roll", fontsize=14)
plt.ylabel("Result", fontsize=14)

#Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

#Display graph
plt.show()                             


#Make a random walk, and plot the points.
rw=RandomWalk()
rw.fillWalk()

#Use a XY chart to visualize the random walk.
rwchart=pygal.XY()
rwchart.title="Random Walk visualization"
rwchart.add("Random Walk", [(rw.xval[n], rw.yval[n]) for n in range(rw.numofpoints)])
rwchart.render_to_file('ex10-2.svg')
