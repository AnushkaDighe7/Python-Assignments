class Arithematic:
    def __init__(self, Value1, Value2):
        
        self.No1 = Value1
        self.No2 = Value2
        Value1 = 0
        Value2 = 0
    
    def Addition(self):
        Ans = 0
        Ans = self.No1+self.No2
        return Ans

    def Substraction(self):
        Ans = 0
        Ans = self.No1-self.No2
        return Ans

    def Multiplication(self):
        Ans = 0
        Ans = self.No1*self.No2
        return Ans

    def Division(self):
        Ans = 0
        Ans = self.No1/self.No2
        return Ans        

def main():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : "))
   
    obj1 = Arithematic(No1,No2)
    
    Ret = obj1.Addition()
    print("Addition is : ",Ret)
    
    Ret = obj1.Substraction()
    print("Substraction is : ",Ret)

    Ret = obj1.Multiplication()
    print("Multiplication is : ",Ret)

    Ret = obj1.Division()
    print("Division is : ",Ret)

    

if __name__ == "__main__":
    main()