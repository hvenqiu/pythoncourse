

def factors(num):
    factorlist = []
    for i in range(1, num+1):
        if num % i == 0:
            # print(i)
            factorlist.append(i)
    return factorlist

# print(factors(10))


def gcf(num1, num2):
    list1 = factors(num1)
    list2 = factors(num2)
    common = []
    for i in list1:
        if i in list2:
            common.append(i)
    return max(common)

print(gcf(150, 138))
