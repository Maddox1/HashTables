import time

# Maddox McElhinney
# I'll begin by making my two hash functions, one intended to be bad, and one intended to be good
# The bad one is based just on the length of the string, and is designed to have thousands of unused buckets
# The good one is based on the length of the string and the unicode value of the first character, with less buckets.
# The good one is designed to have a more even distribution acrsoss fewer buckets for less collisions and wasted memory

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
    hashValue = (len(key) * ord(str(key[0])) + 1) * 1009 # 1009 is an arbitrary prime number to help with distribution
    hashValue %= 19500 # 15000 (length of data) * 1.3 = 19500 buckets
    return hashValue
    
def main():
    data = getData()
    
    start = time.time()
    poorLinkedTable = [[] for i in range(300000)] # 300000 buckets for every possible value from poor hash function
    collisions = 0; used = 0
    for i in range(len(data)):
        poorLinkedTable[poorHashFunction(data[i][0])].append(data[i][0])
        if len(poorLinkedTable[poorHashFunction(data[i][0])]) > 1:
            collisions += 1 # track total collisions
        if len(poorLinkedTable[poorHashFunction(data[i][0])]) == 1:
            used += 1 # track total used buckets
    
    timeTaken = time.time() - start
    unused = 300000 - used
    
    print("Poor Hash Function (titles):")
    print("Total Collisions: " + str(collisions))
    print("Total Unused Buckets: " + str(unused))
    print("Time Taken: " + str(timeTaken) + " seconds")

    start = time.time()
    poorLinkedTable = [[] for i in range(300000)] #refill table with empty buckets
    collisions = 0; used = 0 # reset counters
    for i in range(len(data)):
        poorLinkedTable[poorHashFunction(data[i][1])].append(data[i][1])
        if len(poorLinkedTable[poorHashFunction(data[i][1])]) > 1:
            collisions += 1 # track total collisions
        if len(poorLinkedTable[poorHashFunction(data[i][1])]) == 1:
            used += 1 # track total used buckets
        
    unused = 300000 - used
    timeTaken = time.time() - start  
    
    print("Poor Hash Function (quotes):")
    print("Total Collisions: " + str(collisions))
    print("Total Unused Buckets: " + str(unused))
    print("Time Taken: " + str(timeTaken) + " seconds")

main()