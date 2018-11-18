class Bird(object):
    def __init__(self, name):
        pass

class Duck(Bird):
    def __init__(self, name):
        pass

class Chicken(Bird):
    def __init__(self, name):
        super(Chicken, self).__init__(name)
        self.can_fly = False

class Animal(object):
    def __init__(self, species):
        self.species = 'Bird'

    def getSpecies(self):
        return self. species
