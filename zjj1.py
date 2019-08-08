"""
一个五角数被定义为n(3n-1)/2，其中n=1,2……，
所以，开始的几个数是1、5、12、22、……。
编写一个带下面函数头的函数返回五角数
"""
def getPentagona1Number():
    number = 0
    for n in range(1,100):
        gongshi = (n*(3*n-1))/2
        print(gongshi,end = '、')
        number += 1
        if number % 10 ==0:
            print(end = '\n')
getPentagona1Number()

"""
（求一个整数各个数字的和）编写一个函数，计算一个整数各个数字的和。
使用下面的函数头：def sumDigits (n):
例如：sumDigits (234)返回9（2+3+4）
"""
def sumDigits ():
        input_sum = input('请输入信息：')
        num2 = int(input_sum) % 10
        print(num2)
        num3 = int(input_sum) // 10
        num4 = num3 % 10
        print(num4)
        num5 = int(input_sum) // 100
        print(num5)
        num1 = num2+num4+num5
        print (num1)
                        
sumDigits()

"""
(对三个数进行排序)编写下面的函数，以升序显示三个数
"""
def displaySortedNumber():
        n1 = int(input('one:'))
        n2 = int(input('two:'))
        n3 = int(input('three:'))
        nums = [n1,n2,n3]
        nums.sort()
        print(nums)
displaySortedNumber()

"""
编写一个函数计算指定年数以给定的利率来计算未来投资值
"""
def f(int,mon,year):
        return int *((1+mon/1200)**(year*12))
def main():
        int = eval(input('输入int'))
        mon = eval(input ('输入mon'))
        year = 30
        for i in range(year):
                value = f(int,mon,i+1)
                print(i+1,'年后\t',round(value,2))
main()

"""
编写一个打印字符的函数，按每行指定某个数来打印
打印1~Z的字符，每行打印十个
"""
def pr(ch1,ch2,num):
        a = ord(ch1)
        b = ord(ch2)
        count = 0
        for i in range(a,b):
                a1 = chr(i)
                print(a1,end = " ")
                count += 1
                if count % 10 == 0:
                        print(end = "\n")
pr("1","z",10)

"""
显示从2010年到2020年每年的天数
"""
def numberOfDaysInAYear():
    for i in range(2010,2021):
        if i % 4 == 0 and i%100 != 0:
            print(i , '年',':366天')
        else:
            print(i , '年',':365天')
numberOfDaysInAYear()

"""
用函数计算两点之间的距离
"""
import math
def distance(x1,y1,x2,y2):
    
    d_x = x1 - x2
    d_y = y1 - y2
    #计算两点之间的距离
    distance = math.sqrt(d_x**2 + d_y**2)
    print(distance)
distance(4,9,3,6)


'''
梅森素数：
如果一个素数可以写成2^p-1的形式，其中p是某个正整数，那么这个数就被称作梅森素数
'''
def meisensushu(p):
    q=pow(2,p)-1
    m=2
    if p==2:
        print(p,q)
    for i in range(2,p):
        m=m+1
        if p%i==0:
            break
        if m == p:
            print(p,q)
            
for p in range(1,32):
    meisensushu(p)

'''
当前时间和日期;
调用time.time()返回从1970年1月1日0点开始的毫秒数
'''
import time
print("time.time:%f"%time.time())
time.localtime()
time = time.localtime(time.time())
print("Cuurrent date and time is",time.tm_year,"年",
        time.tm_mon,"月",time.tm_mday,"日",
        time.tm_hour,":",time.tm_min,":",time.tm_sec)

'''
游戏：掷骰子
              
'''
import numpy as np
def dianshu():
        res1 = np.random.choice([1,2,3,4,5,6])
        print("您第一次抛出的点数为:",res1)
        res2 = np.random.choice([1,2,3,4,5,6])
        print("您第二次抛出的点数为:",res2)
        res = res1 + res2
        print("您抛出的两次点数之和为：",res)
        return res
res = dianshu()
if res==2 or res==3 or res==12:
        print("你输了！！！")
elif res==7 or res==11:
        print("你赢了！！！")
else:
        res3 = res
        res = dianshu()
        if res ==7 or res == res3:
                print("你赢了！！！")
        else:
                print("请开始下一局！")