import unittest

def fun(x):
    return None if x is None else x+1
class MyTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(fun(None),None)
    def test2(self):
        self.assertEqual(fun(3),4)
    def test3(self):
        self.assertTrue(fun(0)==1)
    def test3(self):
        self.assertIn(len('123'),[2,3])

class Animal(object): ###object needed in python2 
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def pretty_print(self):
        print("animal name  = %s, species = %s "%(self.name, self.species))
    def get_name(self):
        return self.name


class Dog(Animal):
    count = 0 ## class variable
    def __init__(self, name):  ## self -object
        self.name = name  ## instance variable self.
        Dog.count += 1
        self.__class__.count += 1 ##each instance, 1 class

    def __str__(self):###execute when print has to be string
        return "<Dog name = %s>"%(self.name)
        
    def pretty_print(self):
        print("Dog name  = %s"%(self.name))
    
class Zoo(object):
    def __init__(self):
        self.animals = []
    
    def __len__(self):  ## act like list(tuple, list, dict)
        return len(self.animals)
    



    

if __name__ == '__main__':
    a = Animal('fluffy', 'dog')     ##object
    print(a)
    a.pretty_print()
    #unittest.main()
    d = Dog('puppy')
    d2 = Dog('fido')
    print(d)  ###__str__
    d.pretty_print()
    print(d.get_name())
    print(d.name)
    print(Dog.count)
    zoo = Zoo()
    zoo.animals.append(a)
    zoo.animals.append(d)
    print(len(zoo))
    getattr(d,'name')

    print(getattr(d,'age',10))
    