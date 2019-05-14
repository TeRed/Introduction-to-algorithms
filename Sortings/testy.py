# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 00:13:09 2016

@author: Albert Duź
"""
import random
import time
random.seed()

def selection_sort(List, N):
    for i in range(0, N-1):
        min_index = i
        for j in range(i+1, N):
            if List[j] < List[min_index]:
                min_index = j
    
        List[i], List[min_index] = List[min_index], List[i]

#Bierze kolejne elementy listy i przesuwa je w lewo na własciwe miejsce
def insertion_sort(List, N):
    for i in range(1, N):
        current = List[i]
        for j in range(i-1, -1, -1):
            if List[j] > current:
                List[j+1], List[j] = List[j], List[j+1]
            else:   break

def bubble_sort(List, N):
    for i in range(0, N-1):
        for j in range(0, N-i-1):
            if List[j] > List[j+1]:
                List[j+1], List[j] = List[j], List[j+1]

#Spuszcza element w doł na odpowiednie miejsce
def heap(List, current, end):
    while True:
        child = current * 2 + 1
        if child > end:    break
        if child + 1 <= end and List[child+1] < List[child]:
            child += 1
        if List[current] > List[child]:
            List[current], List[child] = List[child], List[current]
            current = child
        else:   break

def heap_sort(List, N):
        
    for i in range(N-2, -1, -1):
        heap(List, i, N-1)
    
    for i in range(0, N):
        List[0], List[N-i-1] = List[N-i-1], List[0]
        heap(List, 0, N-i-2)
        
    List.reverse()
        
def quick_sort(List, left, right):
    #Liczby są losowe więc za pivota przyjmuję skrajny prawy element
    pivot = List[right]
    j = left

    #i szuka pierwszego elementu mniejszego od pivota
    #j wskazuje pierwszy element większy od pivota i zarazem pominięty przez i
    for i in range(left, right):
        if List[i] < pivot:
            List[i], List[j] = List[j], List[i]
            j += 1
     
    #Ustawienie pivota na własciwe miejsce i wywołanie rekurencyjne funckji
    List[right] = List[j]
    List[j] = pivot

    if left < j-1:
        quick_sort(List, left, j-1)
    
    if j+1 < right:
        quick_sort(List, j+1, right)
        
        

def main():
    N = 32000
    List_of_random_numbers = []

    for i in range (0,N):
        List_of_random_numbers.append(random.randrange(100))
    
        
        
    print("selection sort ", end="")
    List_to_sort = list(List_of_random_numbers)
    
    start_time = time.time()
    #selection_sort(List_to_sort, N)
    print(time.time() - start_time)
    
    
    
    print("Insertion sort")
    List_to_sort = list(List_of_random_numbers)
    
    start_time = time.time()
    #insertion_sort(List_to_sort, N)
    print(time.time() - start_time)
    
    
    
    print("Bubble sort    ")
    List_to_sort = list(List_of_random_numbers)
    
    start_time = time.time()
    #bubble_sort(List_to_sort, N)
    print(time.time() - start_time)
    
    
    
    print("Heap sort")
    List_to_sort = list(List_of_random_numbers)
    
    start_time = time.time()
    heap_sort(List_to_sort, N)
    print(time.time() - start_time)
    
    
    print("Quick sort")
    List_to_sort = list(List_of_random_numbers)
    
    start_time = time.time()
    quick_sort(List_to_sort, 0, N-1)
    print(time.time() - start_time)
    
    
if __name__ == "__main__":
    main()