class Animal(): ###object needed in python2 
    def __init__(self, name, species):
        self.name = name
        self.species = species


if __name__ == '__main__':
    a = Animal('fluffy', 'dog')     ##object
    print(a)