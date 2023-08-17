def Display(No):
    data = range(No)
    for i in data:
       # data = range(No)
        for j in data:
            print(j+1, end = '  ')
        print()

def main():
    Value = 0
    print("Enter the Number")
    Value = int(input())
    Display(Value)

if __name__ == "__main__":
    main()