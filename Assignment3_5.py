import Marvellous_Num

def Listprime(No):
    Addition = 0
    for i in No:
        if Marvellous_Num.chkprime(i):
            Addition += i
    return Addition

def main():
    Data = []

    print("Enter number of elements : ")
    Size = int(input())

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
    result = Listprime(Data)
    print("Addition of prime numbers:", result)

if __name__ == "__main__":
    main()






