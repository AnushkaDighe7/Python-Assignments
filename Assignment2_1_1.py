import Assignment2_1

def main():
    Value1 = int(input("Please Enter the Number : "))
    
    Value2 = int(input("Please Enter the Second Number : "))
   
    
    Result = 0

    Result = Assignment2_1.Add(Value1,Value2)
    print("Addition is : ",Result)

    Result = Assignment2_1.Sub(Value1,Value2)
    print("Substractiom is : ",Result)

    Result = Assignment2_1.Mult(Value1,Value2)
    print("Multiplication is : ",Result)

    Result = Assignment2_1.Div(Value1,Value2)
    print("Division is : ",Result)

if __name__ == "__main__":
    main()