""""
设计一个名为Rectangle的类，来表示矩形。
"""
class Rectangle(object):
    def getArea(self, width = 1,heightd =2):
        self.width = width
        self.heightd= heightd
        print(self.width * self.heightd)
    def getPerimeter(self,width = 1,heightd =2):
        print(self.width *2+self.heightd  * 2)
R = Rectangle()
R.getArea(3,4)
R.getPerimeter()

"""
设计一个名为Account的类
"""
class Account(object):
    def __init__(self):
        self.InterestRate=0
        self.annuallnterestRate=100
        self.Interest=0
    def information(self,id,yu_e):
        self.id=id
        self.yu_e=yu_e
    def getMonthlyInterestRate(self,InterestRate):
        self.InterestRate=InterestRate
    def getMonthlyInterest(self):
        A=self.annuallnterestRate*self.InterestRate
        self.Interest=A
    def withdraw(self):
        print("请输入取钱金额")
        res = input("输入")
        self.annuallnterestRate = self.annuallnterestRate - int(res)
        print("您成功取出",res,"元")
    def deposit(self):
        print("请输入存钱金额")
        res1=input("输入")
        self.annuallnterestRate=self.annuallnterestRate+int(res1)
        print("您成功存入",res1,"元")
        
        print(self.id,"您账户余额为：",self.annuallnterestRate,"利率为：",self.InterestRate,"利息为",self.Interest)
        
E = Account()
E.information(1122,20000)
E.getMonthlyInterestRate(0.045)
E.getMonthlyInterest()
E.withdraw()
E.deposit()

"""
设计一个名为Fan的类表示一个风扇
"""
class Fan(object):
    def __init__(self,speed ,on,radius ,color ):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color
    def fensu(self):
        if self.__speed ==1:
            print("SLOW档")
        elif self.__speed ==2:
            print("MEDIUM档")
        else:
            print("FAST档")
    def kaiguan(self):
        if self.__on =="False":
            print("关闭")
        else:
            print("打开")
    def daxiao(self):
        a = self.__radius 
        print("半径为：%f" % a)
    def yanse(self):
        b= self.__color 
        print("风扇颜色为：%s" % b )
f = Fan(1,"False",5,"blue")
f.fensu()
f.kaiguan()
f.daxiao()
f.yanse()


"""
一个正n边形的边都有同样的长度，所有的角都有同样的度数(即多边形是等角的)
设计一个名为RegularPolygon的类
"""
import math
class RegularPolygon(object):
    def __init__(self,n=3,side=1,x=0,y=0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y
    def getPerimeter(self):
        perimeter = self.__n + self.__side + self.__x + self.__y
        print("多边形的周长为：",perimeter)
    def getArea(self):
        area = (self.__n * (self.__side**2))/4 * (math.tan((3.14/self.__n)))
        print("多边形的面积：",area)



"""
设计一个名为LinearEquation的类，它是2*2的线性方程
"""
class LinearEquation(object):
    def __init__(self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f
        self.x=0
        self.y=0
        self.z=0
    def isSolvable(self):
        s=self.__a*self.__d-self.__b*self.__c
        if s !=0:
            self.s=True
        else:
            self.s=False
    def get(self):
        self.x=(self.__e*self.__d-self.__b*self.__f)/(self.__a*self.__d-self.__b*self.__c)
        self.y=(self.__a*self.__f-self.__e*self.__c)/(self.__a*self.__d-self.__b*self.__c)
    def getX(self):
        self.isSolvable()
        if self.s == True:
            self.get()
            print(self.x)
        else:
            pass
    def getY(self):
        self.isSolvable()
        if self.s == True:
            self.get()
            print(self.y)
        else:
            pass
        
q = LinearEquation(1,2,3,4,5,6)
q.getX()
q.getY()

"""
交叉线
"""
import numpy as np
def get_crossing(s1,s2):
    x1,y1 = s1[0][0],s1[0][1]
    x2,y2 = s1[1][0],s1[1][1]
    x3,y3 = s2[0][0],s2[0][1]
    x4,y4 = s2[1][0],s2[1][1]
    #判断两条直线是否相交，矩阵行列式计算
    a = np.matrix(
        [
            [x2-x1,-(x4-x3)],
            [y2-y1,-(y4-y3)]
        ]
    )
    delta = np.linalg.det(a)
    #不相交,返回两线段
    if np.fabs(delta) < 1e-6:
        print(delta)
        return None        
    #求两个参数lambda和miu
    c = np.matrix(
        [
            [x3-x1,-(x4-x3)],
            [y3-y1,-(y4-y3)]
        ]
    )
    d = np.matrix(
        [
            [x2-x1,x3-x1],
            [y2-y1,y3-y1]
        ]
    )
    lamb = np.linalg.det(c)/delta
    miu = np.linalg.det(d)/delta
    #相交
    if lamb <= 1 and lamb >= 0 and miu >= 0 and miu <= 1:
        x = x3 + miu*(x4-x3)
        y = y3 + miu*(y4-y3)
        return (x,y)
    #相交在延长线上
    else:
        return None
get_crossing(((1,2),(3,3)),((2,2),(2,3)))