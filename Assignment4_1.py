def Power_of_Two(No):
    
    return (2 ** No)
Power_of_Two = lambda No: (2 ** No)

def main():
    print("Enter the number")
    Value  = int(input())

    Ret = Power_of_Two(Value)
    print("power of number is : ",Ret)
    
if __name__ == "__main__":
    main()    