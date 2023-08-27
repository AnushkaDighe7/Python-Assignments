def main():
    List = []

    print("Enter number of elements : ")
    Size = int(input())

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        List.append(Value)

    print("Enter the element that you want to search")    
    Search_No = int(input())
    Frequency = List.count(Search_No)
    
    print("The frequency of number is ",Frequency)    
    
if __name__ == "__main__":
    main()     