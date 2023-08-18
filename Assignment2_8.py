def Display(No):
    data = range(1,No+1)
    for i in data:
        data = range(1,i+1)
        for j in data:
            print(j, end = '  ')
        print()

def main():
    Value = 0
    print("Enter the Number")
    Value = int(input())
    Display(Value)

if __name__ == "__main__":
    main()