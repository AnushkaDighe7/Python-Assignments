def SumFactors(No):
    iCnt = 0
    iSum = 0
    data = range(1,int(No/2)+1)
    for i in data:
        if(No % i == 0):
            iSum = iSum + i
    return iSum

def main():
    Value = 0
    bRet = 0
    print("Enter the Number")
    Value = int(input())

    bRet = SumFactors(Value)
    print("Summation of factors is : ",bRet)
    
if __name__ == "__main__":
    main()       