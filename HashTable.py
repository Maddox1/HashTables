import random
import time

# Maddox McElhinney
# I'll begin by making my two hash functions, one intended to be bad, and one intended to be good
# The bad one is based just on the length of the string, and is designed to have thousands of unused buckets
# The good one is based on the unicode values of each character in the string,
# with less buckets to minimize wasted memory

# For this example I will use the poor hash function with a linear probing style hash table

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
    hashValue = 0
    for char in key: # sum unicode values of each character in the key
        hashValue = (hashValue * 31 + ord(char) + hashValue % 11) % 19500
    return hashValue
    
def main():
    data = getData()
    
    start = time.time()
    badLinearTable = [None] * 750000
    collisions = 0; used = 0
    for i in range(len(data)):
        index = poorHashFunction(data[i][0])
        while badLinearTable[index] != None: # if bucket is filled
            collisions += 1 # collision detected
            index = (index + 1) % 750000 # linear probe to next bucket
        badLinearTable[index] = data[i][0] # empty bucket found, insert data
        used += 1 # we use the bucket
    
    timeTaken = time.time() - start
    unused = 750000 - used
    
    print("Poor Linear Probing Hash Function (titles):")
    print("Total Collisions: " + str(collisions))
    print("Total Unused Buckets: " + str(unused))
    print("Time Taken: " + str(timeTaken) + " seconds")

    start = time.time()
    badLinearTable = [None] * 750000
    collisions = 0; used = 0
    for i in range(len(data)):
        index = poorHashFunction(data[i][1])
        while badLinearTable[index] != None: # if bucket is filled
            collisions += 1 # collision detected
            index = (index + 1) % 750000 # linear probe to next bucket
        badLinearTable[index] = data[i][1] # empty bucket found, insert data
        used += 1 # we use the bucket
        
    unused = 750000 - used
    timeTaken = time.time() - start  
    
    print("Poor Linear Probing Hash Function (quotes):")
    print("Total Collisions: " + str(collisions))
    print("Total Unused Buckets: " + str(unused))
    print("Time Taken: " + str(timeTaken) + " seconds")

main()