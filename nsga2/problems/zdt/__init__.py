"""Module with definition of ZDT problem interface"""

from nsga2.individual import Individual
from nsga2.problems import Problem
import random
import functools

class ZDT(Problem):

    def __init__(self, zdt_definitions):
        self.zdt_definitions = zdt_definitions
        self.max_objectives = [None, None]
        self.min_objectives = [None, None]
        self.problem_type = None
        self.factor = self.n = self.zdt_definitions.n  # define  factor  dimension 
        self.features_min = self.zdt_definitions.features_min
        self.features_max = self.zdt_definitions.features_max

    def __dominates(self, individual2, individual1): #individual1 is self, individual2 is another 
        worse_than_other = True 
        for i in  range(len(individual1.objectives)):
            worse_than_other = worse_than_other and  individual1.objectives[i] <= individual2.objectives[i]
        return worse_than_other 

    def generateIndividual(self):
        individual = Individual()
        individual.features = []
        for i in range(self.n):
            individual.features.append(random.uniform(self.zdt_definitions.features_min[i],self.zdt_definitions.features_max[i]))
        individual.dominates = functools.partial(self.__dominates, individual1=individual)
        return individual

    def calculate_objectives(self, individual):   
        individual.objectives = []
        individual.objectives.append(self.zdt_definitions.f1(individual))
        individual.objectives.append(self.zdt_definitions.f2(individual))
        for i in range(2):
            if self.min_objectives[i] is None or individual.objectives[i] < self.min_objectives[i]:
                self.min_objectives[i] = individual.objectives[i]
            if self.max_objectives[i] is None or individual.objectives[i] > self.max_objectives[i]:
                self.max_objectives[i] = individual.objectives[i]
