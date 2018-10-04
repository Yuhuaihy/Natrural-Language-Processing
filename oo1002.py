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


class Dog(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def pretty_print(self):
        print("Dog name  = %s, species = %s "%(self.name, self.species))


    

if __name__ == '__main__':
    a = Animal('fluffy', 'dog')     ##object
    print(a)
    a.pretty_print()
    unittest.main()