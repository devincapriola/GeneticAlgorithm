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

    # Building the Crossover method
    def mix(self, dna1, dna2):
        self.dna = dna1.copy()

        for i in range(self.dnaLength - 1):
            if np.random.rand() <= 0.5:
                previous = self.dna[i]
                inx = self.dna.index(dna2[i])
                self.dna[inx] = previous
                self.dna[i] = dna2[i]

        # Random Partial Mutations 1
        for i in range(self.dnaLength - 1):
            if np.random.rand() <= 0.1:
                previous = self.dna[i]
                rnd = np.random.randint(1, self.dnaLength)
                inx = self.dna.index(rnd)
                self.dna[inx] = previous
                self.dna[i] = rnd

            # Random Partial Mutations 2
            elif np.random.rand() <= 0.1:
                rnd = np.random.randint(1, self.dnaLength)
                prevInx = self.dna.index(rnd)
                self.dna.insert(i, rnd)

                if i >= prevInx:
                    self.dna.pop(prevInx)
                else:
                    self.dna.pop(prevInx + 1)


# Initializing the main code
populationSize = 50
mutationRate = 0.1
nSelected = 5

env = Environment()
dnaLength = len(env.planets)
population = list()
