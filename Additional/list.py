# -*- coding: utf-8 -*-
"""
@author: Albert Duź
"""

class Node:
    
    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.next = None
        self.prev= None
        
    def __str__(self):
        return str(self.name) + ": " + str(self.points) + " points"
        
class List:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_at_beginning(self, name, points):
        if not self.head:
            new_node = Node(name, points)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(name, points)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def add_at_end(self, name, points):
        if not self.tail:
            new_node = Node(name, points)
            self.tail = new_node
            self.head = new_node
        else:
            new_node = Node(name, points)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    def add_at_n_position(self, name, points, position):
        if position <= 0:
            print("Impossible. List start with element 1")
            return
        n = self.head
        x = 1 #count positions of list
        while n and x != position - 1:
            n = n.next
            x += 1
        if position == 1:
            self.add_at_beginning(name, points)
        elif not n:
            self.add_at_end(name, points)
        else:
            new_node = Node(name, points)
            new_node.prev = n
            new_node.next = n.next
            n.next.prev = new_node
            n.next = new_node
            
    def remove_from_end(self):
        n = self.tail
        self.tail = self.tail.prev
        n.prev = None
        self.tail.next = None
        
    def remove_from_beggining(self):
        n = self.head
        self.head = self.head.next
        n.next = None
        self.head.prev = None
        
    def find_highest_score(self):
        max = self.head
        n = self.head
        while n:
            if n.points > max.points: max = n
            n = n.next
        if max == None:
            print("No scores in database!")
        else:
            print("Highest score has " + str(max.name) + ": " + str(max.points) + " points")
            
    def print_list(self):
        n = self.head
        while n:
            print(n)
            n = n.next
            
    def print_list_reverse(self):
        n = self.tail
        while n:
            print(n)
            n = n.prev
def main():
    list = List()
    list.add_at_beginning("Jan", 0)
    list.add_at_beginning("Mateusz", 20)
    list.add_at_end("Anna", 17)
    list.add_at_end("Katarina", 15)
    list.add_at_n_position("Janusz", 14, 25)
    list.add_at_n_position("Grażyna", 11, 0)
    list.add_at_n_position("Grażyna", 9, 1)
    list.add_at_n_position("Marek", 8, 2)
    list.add_at_n_position("Tomek", 10, 5)
    list.add_at_n_position("Tomasz", 19, 1)
    list.remove_from_end()
    list.remove_from_beggining()
    list.remove_from_beggining()
    
    print("")
    print("List:")
    list.print_list()
    print("")
    print("Reverse list:")
    list.print_list_reverse()
    print("")
    list.find_highest_score()
    
if __name__ == "__main__":
    main()