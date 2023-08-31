class Circle:
    PI=3.14
    def __init__(self, Value1):
        self.No1 = Value1
        
        Radius = 0.0
        Area = 0.0
        Circumference = 0.0
    
    def Accept(self):
        print("Value is : ",self.No1)

    def Area(self):
        Ans = 0
        Ans = Circle.PI*self.No1**2
        return Ans

    def Circumference(self):
        Ans = 0
        Ans = 2*Circle.PI*self.No1
        return Ans


def main():
    No1 = int(input("Enter the Radius : "))
    obj1 = Circle(No1)
    
    Ret = obj1.Area()
    print("Area of Circle is : ",Ret)

    Ret = obj1.Circumference()
    print("Circumference of Circle is : ",Ret)
    
if __name__ == "__main__":
    main()