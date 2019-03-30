import pygal
from random import randint

class Die():
    """A class representing a single die."""

    def __init__(self, numsides=6):
        """Assume a six-sided die."""
        self.numsides=numsides

    def roll(self):
        """"Return a random value between 1 and number of sides."""
        return randint(1, self.numsides)


#Create 2 six sided die
die1=Die()
die2=Die()

#Make some rolls, and store results in a list
results=[die1.roll() * die2.roll() for num in range(1000000)]

#Analyze the results
frequencies=[results.count(value) for value in range(2,die1.numsides*die2.numsides+1)]

#Visualize the results
hist=pygal.Bar()

#Setting labels of title and axis
hist.title="Results of rolling two six sided dice 1000000 times"
hist.x_labels=[str(x) for x in range(2,die1.numsides*die2.numsides+1)]
hist.x_title="Result"
hist.y_title="Frequency of Result"

#Create graph
hist.add('D6*D6', frequencies)
hist.render_to_file('ex09.svg')
