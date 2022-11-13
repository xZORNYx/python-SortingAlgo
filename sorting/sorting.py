# Zorny
import random

# Some of the most famous sorting algorithme in python
# The code isn't optimized but at least it works

def generateArray(length, min, max):
    array = []
    for val in range(length):
        array.append(random.randint(min, max))
    return array

def bubbleSort(array):
    arr_length = len(array)
    if arr_length > 1:
        doContinue = True
        while doContinue:
            doContinue = False
            for idx, val in enumerate(array):
                if idx < arr_length-1:
                    if val > array[idx+1]:
                        array[idx] = array[idx+1]
                        array[idx+1] = val
                        doContinue = True
    
    return array

def selectionSort(array):
    arr_length = len(array)
    if arr_length <= 1:
        sorted_array = array
    else:
        sorted_array = []
        for i in range(arr_length):
            smaller = None
            for val in array:
                if smaller is None or val < smaller:
                    smaller = val
            sorted_array.append(smaller)
            array.remove(smaller)
            
    return sorted_array

def doubleSelectionSort(array):
    arr_length = len(array)
    if arr_length <= 1:
        sorted_array = array
    else:
        sorted_array = []
        for i in range(arr_length):
            smaller = None
            larger = None
            for val in array:
                if smaller is None or val < smaller:
                    smaller = val
                elif larger is None or val > larger:
                    larger = val
            if larger is not None:
                sorted_array.insert(-i, larger)
                array.remove(larger)
            if smaller is not None:
                sorted_array.insert(i, smaller)
                array.remove(smaller)
        return sorted_array

def cycleSort(array):
    arr_length = len(array)
    if arr_length > 1:
        current = array[0]
        array[0] = None
        while array[0] == None:
            count = 0
            for val in array:
                if val is not None:
                    if val < current:
                        count+=1
            tmp = current
            current = array[count]
            array[count] = tmp
    return array