def Summation(n):
    
    sum = 0
    for No in str(n): 
        sum += int(No)      
    return sum    

def main():
    Value = 0
    bRet = 0
    print("Enter the Number")
    Value = int(input())

    bRet = Summation(Value)
    print("Addition of digits are : ",bRet)

if __name__ == "__main__":
    main()    
