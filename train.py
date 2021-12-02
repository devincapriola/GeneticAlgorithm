# Space Discover: Genetic Algorithms - Training File 

# Importing the libraries
import numpy as np
from environment import Environment

# Creating the bots
# dna_size = 3,1,2,0
# fitness_size = 3,1,2,0
class Route():
    def __init__(self, dnaLength):
        self.dnaLength = dnaLength
        self.dna = list()
        self.distance = 0
