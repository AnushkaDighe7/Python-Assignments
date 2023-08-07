def ChkNumber(No):
    if(No > 0):
        return 0
    elif(No == 0):
        return 1
    else:
        return -1

def main():
    Value = 0
    bRet = 0
    print("Enter the Number")
    Value = int(input())

    bRet = ChkNumber(Value)
    if(bRet == 0):
        print("Positive Number")
    elif(bRet == 1):
        print("Zero")    
    else:
        print("Negative Number")    

if __name__ == "__main__":
    main()              