def Display(No):
    data = range(No,0,-1)
    for i in data:
        data = range(0,i)
        for j in data:
            print('*', end = '  ')
        print()

def main():
    Value = 0
    print("Enter the Number")
    Value = int(input())
    Display(Value)

if __name__ == "__main__":
    main()