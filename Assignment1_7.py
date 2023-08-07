def DivisibleByFive(No):
   
    Result = No % 5
    if(Result == 0):
        return True
    else:
        return False

def main():
    Value = 0
    bRet = 0
    print("Please Enter the Number")
    Value = int(input())

    bRet = DivisibleByFive(Value)
    if(bRet == True):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()   