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
