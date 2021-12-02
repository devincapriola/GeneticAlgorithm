# Space Discover: Genetic Algorithms - Training File 

# Importing the libraries
import numpy as np
from environment import Environment

# Creating the bots
class Route():
    def __init__(self, dnaLength):
        self.dnaLength = dnaLength
        self.dna = list()
        self.distance = 0

        # Initialize the random dna
        for i in range(self.dnaLength - 1):
            rnd = np.random.randint(1, self.dnaLength)
            while rnd in self.dna:
                rnd = np.random.randint(1, self.dnaLength)
            self.dna.append(rnd)
        self.dna.append(0)
