class ProblemDefinitions():
    n = None
    features_min = None
    features_max = None
    
    def __init__(self):
        raise NotImplementedError

    def f1(self, individual):
        raise NotImplementedError

    def f2(self, individual):
        raise NotImplementedError

    def perfect_pareto_front(self):
        raise NotImplementedError

