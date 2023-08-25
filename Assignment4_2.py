def Multiplication(No1,No2):
    
    return (No1 * No2)
Multiplication= lambda No1,No2: (No1 * No2)

def main():
    print("Enter the First number")
    Value1  = int(input())

    print("Enter the second number")
    Value2  = int(input())

    Ret = Multiplication(Value1,Value2)
    print("Multiplication is : ",Ret)
    
if __name__ == "__main__":
    main()    