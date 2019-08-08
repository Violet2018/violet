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


"""
设计一个名为Fan的类表示一个风扇
"""
class Fan(object):
    def __init__(self,speed ,on,radius ,color ):
        self._speed = speed
        self._on = on
        self._radius = radius
        self._color = color
    def methods(self):
        if self._speed ==1:
            print("SLOW档")
        elif self._speed ==2:
            print("MEDIUM档")
        else:
            print("FAST档")
    def On(self):
        if self._on =="False":
            print("关闭")
        else:
            print("打开")
    def Radius(self):
        a = self._radius 
        print("半径为：%f" % a)
    def Color(self):
        b= self._color 
        print("风扇颜色为：%s" % b )
f = Fan(1,"FAST",5,"蓝色")
f.methods()
f.On()
f.Radius()
f.Color()


"""
一个正n边形的边都有同样的长度，所有的角都有同样的度数(即多边形是等角的)
设计一个名为RegularPolygon的类
"""
import math
class RegularPolygon(object):
    def __init__(self,n=3,side=1,x=0,y=0):
        self.n = n
        self.side = side
        self.x = x
        self.y = y
    def getPerimeter(self):
        perimeter = self.n + self.side + self.x + self.y
        print("多边形的周长为：",perimeter)
    def getArea(self):
        area = (self.n * (self.side**2))/4 * (math.tan((3.14/self.n)))
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
        z=self.__a*self.__d-self.__b*self.__c
        if z !=0:
            self.z=True
        else:
            self.z=False
    def get(self):
        self.x=(self.__e*self.__d-self.__b*self.__f)/(self.__a*self.__d-self.__b*self.__c)
        self.y=(self.__a*self.__f-self.__e*self.__c)/(self.__a*self.__d-self.__b*self.__c)
    def getX(self):
        self.isSolvable()
        if self.z == True:
            self.get()
            print(self.x)
        else:
            pass
    def getY(self):
        self.isSolvable()
        if self.z == True:
            self.get()
            print(self.y)
        else:
            pass
        
qwe=LinearEquation(10,2,3,7,8,1)
qwe.getX()
qwe.getY()

"""
交叉线
"""
import numpy as np
def get_crossing(s1,s2):
    xa,ya = s1[0][0],s1[0][1]
    xb,yb = s1[1][0],s1[1][1]
    xc,yc = s2[0][0],s2[0][1]
    xd,yd = s2[1][0],s2[1][1]
    #判断两条直线是否相交，矩阵行列式计算
    a = np.matrix(
        [
            [xb-xa,-(xd-xc)],
            [yb-ya,-(yd-yc)]
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
            [xc-xa,-(xd-xc)],
            [yc-ya,-(yd-yc)]
        ]
    )
    d = np.matrix(
        [
            [xb-xa,xc-xa],
            [yb-ya,yc-ya]
        ]
    )
    lamb = np.linalg.det(c)/delta
    miu = np.linalg.det(d)/delta
    #相交
    if lamb <= 1 and lamb >= 0 and miu >= 0 and miu <= 1:
        x = xc + miu*(xd-xc)
        y = yc + miu*(yd-yc)
        return (x,y)
    #相交在延长线上
    else:
        return None
get_crossing(((1,2),(3,4)),((1,4),(2,3)))