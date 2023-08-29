from functools import reduce

def CheckPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def multiply(No):
    return No*2

def iMax(A,B):
    return A if A > B else B

def main():
    Data = []

    print("Enter number of elements : ")
    Size = int(input())

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
    
    print("Input data : ",Data)
    
    output = list(filter(CheckPrime,Data))
    print("Output after filter : ",output)

    moutput = list(map(multiply,output))
    print("Output after map : ",moutput)

    result = reduce(iMax,moutput)
    print("Output after reduce : ",result)

if __name__ == "__main__":
    main()