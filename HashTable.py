from math import floor
import random
import time

# Maddox McElhinney
# I'll begin by making my two hash functions, one intended to be bad, and one intended to be good
# The bad one is based just on the length of the string, and is designed to have thousands of unused buckets
# The good one is based on the sum of the unicode values of the characters in the string, and is designed to minimize collisions

# For this example I will use the better hash function and linear probing

def getData():
    data = []
    with open("MOCK_DATA.csv", "r", encoding="utf-8") as file:
        file.readline() # skip header line
        for line in file:
            data.append(line.strip().split(",")[0:9:8]) # fill out list with data
    return data

def poorHashFunction(key):
    return (len(key) // 10 * 999 + 1) % 750000 # further unoptimized by adding addtional buckets which will not be filled! 
                                               # also added a little division which should encourage more collisions.

def hashFunction(key):
    return floor(19500 * (sum(ord(char) for char in key) * 0.6180339887 % 1)) # .6180339887 is the golden ratio
    
def main():
    data = getData()
    
    start = time.time()
    betterLinearTable = [None] * 19500
    collisions = 0; used = 0
    for i in range(len(data)):
        index = hashFunction(data[i][0])
        while betterLinearTable[index] != None: # if bucket is filled
            collisions += 1 # collision detected
            index = (index + 1) % 19500 # linear probe to next bucket
        betterLinearTable[index] = data[i][0] # empty bucket found, insert data
        used += 1 # we use the bucket
    
    timeTaken = time.time() - start
    unused = 19500 - used
    
    print("Better Linear Probing Hash Function (titles):")
    print("Total Collisions: " + str(collisions))
    print("Total Unused Buckets: " + str(unused))
    print("Time Taken: " + str(timeTaken) + " seconds")

    start = time.time()
    betterLinearTable = [None] * 19500
    collisions = 0; used = 0
    for i in range(len(data)):
        index = hashFunction(data[i][1])
        while betterLinearTable[index] != None: # if bucket is filled
            collisions += 1 # collision detected
            index = (index + 1) % 19500 # linear probe to next bucket
        betterLinearTable[index] = data[i][1] # empty bucket found, insert data
        used += 1 # we use the bucket
    
    timeTaken = time.time() - start
    unused = 19500  - used
        
    print("Better Linear Probing Hash Function (quotes):")
    print("Total Collisions: " + str(collisions))
    print("Total Unused Buckets: " + str(unused))
    print("Time Taken: " + str(timeTaken) + " seconds")

main()