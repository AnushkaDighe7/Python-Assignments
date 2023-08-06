def ChkNum(No):
   
    Result = No % 2
    if(Result == 0):
        return True
    else:
        return False

def main():
    Value = 0
    bRet = 0
    print("Please Enter the Number")
    Value = int(input())

    bRet = ChkNum(Value)
    if(bRet == True):
        print("Number is Even")
    else:
        print("Number is Odd")

if __name__ == "__main__":
    main()       
