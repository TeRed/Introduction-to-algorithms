# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Person:
    def __init__(self, name, father, mother):
        self.name = name
        self.father = father
        self.mother = mother
        self.childrens = []
        self.partner = None

    def add_child(self, name):
        self.childrens.append(name)
        
    def add_partner(self, partner):
        self.partner = partner
        
class Tree:
    def __init__(self):
        self.people = []
        
    def add(self, person):
        for i in self.people:
            if(i == person.father or i == person.mother):
                person.add_child(i)
        self.people.append(person)
                    
    def repair(self):
        to_remove = []
        for i in self.people:
            if(not i.childrens):
                to_remove.append(i)
        
        for i in to_remove:
            i.father.childrens.remove(i)
            i.mother.childrens.remove(i)
            self.people.remove(i)
            
    def remove(self, person):
        person.father.childrens.remove(person)
        person.mother.childrens.remove(person)
        person.partner.partner = None
        for i in person.childrens:
            i.father = None
            i.mother = None
            
        self.people.remove(person)
        
    def show(self):
        for i in self.people:
            print("Name: " + str(i.name))
            print("Partner: " + str(i.partner))
            if i.father == None or i.mother == None:
                print("Nic")
            else:
                print("Parents: " + str(i.father.name) + " " + str(i.mother.name))
            print("Childs: " + str(i.childrens))
            
def main():
    X = Tree()
    a = Person("Jan", None, None)
    b = Person("Zosia", None, None)
    c = Person("Mateusz", a, None)
    d = Person("Kasia", c, b)
    
    X.add(a)
    X.add(b)
    X.add(c)
    X.add(d)
    X.show()
    
if __name__ == "__main__":
    main()
