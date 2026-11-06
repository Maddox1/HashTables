import random
import time

# Maddox McElhinney
# I'll begin by making my two hash functions, one intended to be bad, and one intended to be good
# The bad one is based just on the length of the string, and is designed to have thousands of unused buckets
# The good one is based on the unicode values of each character in the string,
# with less buckets to minimize wasted memory

# For this example and the next I will be using a linked list style hash table,
# By comprising the table of lists, I can make collisions easy to handle by just appending it to the list

def getData():
    data = []
    with open("MOCK_DATA.csv", "r", encoding="utf-8") as file:
        file.readline() # skip header line
        for line in file:
            data.append(line.strip().split(",")[0:9:8]) # fill out list with data
    return data

def poorHashFunction(key):
    return (len(key) * 999 + 1) % 300000 

def hashFunction(key):
    hashValue = 0
    for char in key: # sum unicode values of each character in the key
        hashValue = (hashValue * 31 + ord(char) + hashValue % 11) % 19500
    return hashValue
    
def main():
    data = getData()
    
    start = time.time()
    betterLinkedTable = [[] for i in range(19500)] # 19500 buckets for every possible value from good hash function
    collisions = 0; used = 0
    for i in range(len(data)):
        betterLinkedTable[hashFunction(data[i][0])].append(data[i][0])
        if len(betterLinkedTable[hashFunction(data[i][0])]) > 1:
            collisions += 1 # track total collisions
        if len(betterLinkedTable[hashFunction(data[i][0])]) == 1:
            used += 1 # track total used buckets
    
    timeTaken = time.time() - start
    unused = 19500 - used
    
    print("Good Hash Function (titles):")
    print("Total Collisions: " + str(collisions))
    print("Total Unused Buckets: " + str(unused))
    print("Time Taken: " + str(timeTaken) + " seconds")

    start = time.time()
    betterLinkedTable = [[] for i in range(19500)] #refill table with empty buckets
    collisions = 0; used = 0 # reset counters
    for i in range(len(data)):
        betterLinkedTable[hashFunction(data[i][1])].append(data[i][1])
        if len(betterLinkedTable[hashFunction(data[i][1])]) > 1:
            collisions += 1 # track total collisions
        if len(betterLinkedTable[hashFunction(data[i][1])]) == 1:
            used += 1 # track total used buckets
        
    unused = 19500 - used
    timeTaken = time.time() - start  
    
    print("Good Hash Function (quotes):")
    print("Total Collisions: " + str(collisions))
    print("Total Unused Buckets: " + str(unused))
    print("Time Taken: " + str(timeTaken) + " seconds")

main()