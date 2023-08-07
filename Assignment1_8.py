def Display(No):
    data = range(No)
    for no in data:
        print("*")

def main():
    Value = 0
    print("Enter the Number")
    Value = int(input())
    Display(Value)

if __name__ == "__main__":
    main()