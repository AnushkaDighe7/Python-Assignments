def Factorial(No):
    Fact = 1
    for i in range(1,No+1):    
        Fact = Fact*i   
        print("The factorial is",Fact)      

def main():
    Value = 0
    print("Enter the Number")
    Value = int(input())
    Factorial(Value)

if __name__ == "__main__":
    main()