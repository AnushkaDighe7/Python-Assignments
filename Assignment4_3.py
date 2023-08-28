from functools import reduce

Select = lambda No: (No >= 70 and No <= 90)
Increase = lambda No: No+10
Product = lambda A,B: A*B

def filterX(Task, Elements):
    Result = []
    for no in Elements:
        if(Task(no) == True):
            Result.append(no)
    return Result

def mapX(Task, Elements):
    Result = []
    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)
    return Result

def main():
    Data = []

    print("Enter number of elements : ")
    Size = int(input())

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
    
    print("Input data : ",Data)
    output = list(filterX(Select,Data))
    print("Output after filter : ",output)

    moutput = list(mapX(Increase,output))
    print("Output after map : ",moutput)

    result = reduce(Product,moutput)
    print("Output after reduce : ",result)

if __name__ == "__main__":
    main()