class Demo:
    Value = 0
    def __init__(self, No1, No2):     
        
        self.Value1 = No1
        self.Value2 = No2

    def Fun(self):
        print("Value of No1 : ",self.Value1)
        print("Value of No2 : ",self.Value2)

    def Gun(self):
        print("Value of No1 : ",self.Value1)
        print("Value of No2 : ",self.Value2)    

def main():
    print("Demonstration of Object Orientation")

    obj1 = Demo(11,21)  
    obj2 = Demo(51,101)  

    obj1.Fun()  
    obj2.Fun() 

    obj1.Gun()  
    obj2.Gun() 

if __name__ == "__main__":
    main()