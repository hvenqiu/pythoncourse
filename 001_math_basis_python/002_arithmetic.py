def mysum(num):
    running_sum = 0
    for i in range(num+1):
        running_sum += i
    return running_sum

# print(mysum(100))

def mysum2(num):
    running_sum = 0
    for i in range(1, num+1):
        running_sum += i**2+1
    return running_sum

# print(mysum2(20))

def myaverage(numlist):
    return sum(numlist)/len(numlist)

# print(myaverage([1, 2, 3, 4, 5]))   

d=[53, 28, 54, 84, 65, 60, 22, 93, 62, 27, 16, 25, 74, 42, 
4, 42, 15, 96, 11, 70, 83, 97, 75]
print(myaverage(d))