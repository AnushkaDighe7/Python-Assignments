def Add(No1,No2):
    Result = 0
    Result = No1 + No2
    return Result

def main():
    Value1 = 0
    Value2 = 0
    Ans = 0
    print("Enter the First Number")
    Value1 = int(input())

    print("Enter the Second Number")
    Value2 = int(input())

    Ans = Add(Value1,Value2)

    print("Addition is :",Ans)

if __name__ == "__main__":
    main()        