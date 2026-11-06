from math import floor
import random
import time

# Maddox McElhinney
# The hash function I'm using is a rolling sum hash function, which should help minimize collisions

# For my final test, I want to combine the best traits of previous experiments.
# I will use my first good hash function, as it seemed to lead to the least collisions
# I will try to combine linked lists with linear probing to see if that can make a hash table more efficient
# A bucket will be full if it has 2 elements in it, and if a bucket is full, I will linear probe to the next bucket
# This find a decent middle ground of collisions and unused buckets,
# as the linked list will allow for more than one element in a bucket, 
# and the linear probing will allow for more buckets to be used

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
    for char in key:
        hashValue = (hashValue * 31 + ord(char)) % 19683
    return hashValue
    
def main():
    data = getData()
    
    start = time.time()
    linearTable = [[] for _ in range(19683)]
    collisions = 0; used = 0
    for i in range(len(data)):
        if len(linearTable[hashFunction(data[i][0])]) > 1: # if bucket has 2 elements, linear probe
            collisions += 1 # collision detected
            index = (hashFunction(data[i][0]) + 1) % 19683 # linear probe to next bucket
            while len(linearTable[index]) > 1: # if bucket has 2 elements, linear probe
                collisions += 1 # collision detected
                index = (index + 1) % 19683 # linear probe to next bucket
            linearTable[index].append(data[i][0]) # empty bucket found, insert data
        else:
            linearTable[hashFunction(data[i][0])].append(data[i][0]) # bucket with less than 2 values found, insert data
        if len(linearTable[hashFunction(data[i][0])]) == 1: # if bucket has 1 element, we used a bucket
            used += 1 # we use the bucket 

    timeTaken = time.time() - start
    unused = 19683 - used
    
    print("Final Hash Test (titles):")
    print("Total Collisions: " + str(collisions))
    print("Total Unused Buckets: " + str(unused))
    print("Time Taken: " + str(timeTaken) + " seconds")

    start = time.time()
    linearTable = [[] for _ in range(19683)]
    collisions = 0; used = 0
    for i in range(len(data)):
        if len(linearTable[hashFunction(data[i][1])]) > 1: # if bucket has 2 elements, linear probe
            collisions += 1 # collision detected
            index = (hashFunction(data[i][1]) + 1) % 19683 # linear probe to next bucket
            while len(linearTable[index]) > 1: # if bucket has 2 elements, linear probe
                collisions += 1 # collision detected
                index = (index + 1) % 19683 # linear probe to next bucket
            linearTable[index].append(data[i][1]) # empty bucket found, insert data
        else:
            linearTable[hashFunction(data[i][1])].append(data[i][1]) # bucket with less than 2 values found, insert data
        if len(linearTable[hashFunction(data[i][1])]) == 1: # if bucket has 1 element, we used a bucket
            used += 1 # we use the bucket 

    timeTaken = time.time() - start
    unused = 19683 - used
    
    print("Final Hash Test (titles):")
    print("Total Collisions: " + str(collisions))
    print("Total Unused Buckets: " + str(unused))
    print("Time Taken: " + str(timeTaken) + " seconds")

main()