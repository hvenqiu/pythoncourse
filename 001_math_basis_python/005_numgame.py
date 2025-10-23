from  random import randint
from math import sqrt

def randomgame():
    num = randint(1,100)
    # print(num)
    name=input("请问你的姓名：")
    print("欢迎 %s 来猜数字游戏！" % name)
    while True:
        guess = int(input("请输入你猜的数字(1-100)："))
        if guess == num:
            print("恭喜你，猜对了！")
            break
        elif guess > num:
            print("你猜的数字太大了！")
        else:
            print("你猜的数字太小了！")


# randomgame()

def average(a,b):
    return (a+b)/2

def squareroot(num,low,high):
    '''采用猜数策略来计算一个数的平方根'''
    for i in range(20):
        guess = average(low,high)
        if guess**2 == num:
            return guess
        elif guess**2 > num:
            high = guess
        else:
            low = guess
    print("计算结果为：%f" % guess)

# squareroot(60,7,8)
# squareroot(200,14,15)
# squareroot(1000,30,40)


def equation(a,b,c,d):
    if a-c == 0:
        result = None
        # print("无解")
    elif a-c != 0:
        result = (d-b)/(a-c)
        # print("方程有解：%f" % result)
    return result

# equation(16,2,3,5)
# x=equation(2,5, 0,13)
# print(x)



def quad(a,b,c):
    '''求解二次方程 ax^2+bx+c=0 的根'''
    if a == 0:
        result = None, None
        print("不是二次方程")
    elif a != 0:
        delta = b**2 - 4*a*c
        if delta < 0:
            result = None, None
            print("无解")
        elif delta >= 0:
            result = (-b - sqrt(delta))/(2*a), (-b + sqrt(delta))/(2*a)
            print("方程有解：%f %f" % result)
    return result   

# x1,x2 = quad(2,7,-15)
# print(2*x1**2+7*x1-15)
# print(2*x2**2+7*x2-15)


def g(x):
    return 6*x**3 + 31*x**2 + 3*x -10

def plug():
    x = -100
    while x <= 100:
        if g(x) == 0:
            print("方程有解：%f" % x)
        x += 1

plug()

