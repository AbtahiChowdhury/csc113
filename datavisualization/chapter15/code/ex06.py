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


#Create six sided die
die=Die()

#Make some rolls, and store results in a list
results=[die.roll() for num in range(1000)]

#Analyze the results
frequencies=[results.count(value) for value in range(1,die.numsides+1)]

#Visualize the results
hist=pygal.Bar()

#Setting labels of title and axis
hist.title="Results of rolling one six sided die 1000 times"
hist.x_labels=[str(x) for x in range(1,die.numsides+1)]
hist.x_title="Result"
hist.y_title="Frequency of Result"

#Create graph
hist.add('D6', frequencies)
hist.render_to_file('ex06.svg')
