def main():
    List = []

    print("Enter number of elements : ")
    Size = int(input())

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        List.append(Value) 
    
    print("Minimum number is : ",min(List))  

if __name__ == "__main__":
    main()       