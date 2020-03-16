"""Module with definition of Problem interface"""

class Problem(object):
    
    def __init__(self):
        self.max_objectives = list()
        self.min_objecives =  list()
        self.problem_type = None
        self.factor = 0              # factor  count 
        self.features_min = list()         # every factor min value 
        self.features_max = list()       #every factor max value   
        
    def generateIndividual(self):
        
        raise NotImplementedError
        
    def calculate_objectives(self, individual):
        
        raise NotImplementedError
