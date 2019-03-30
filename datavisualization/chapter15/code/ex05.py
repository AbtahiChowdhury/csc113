import matplotlib.pyplot as plt
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


#Keep making new walks, as long as the program is active.
while True:

    #Make a random walk, and plot the points.
    rw = RandomWalk(5000)
    rw.fillWalk()

    #Set size of plotting window.
    plt.figure(figsize=(10, 6))

    #Create plot of walk
    plt.plot(rw.xval, rw.yval, linewidth=1)

    #Display graph
    plt.show()

    #Prompt to keep running
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
