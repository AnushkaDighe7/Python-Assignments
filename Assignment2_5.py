def prime(No):
    if No <= 1:
        return False
    for i in range(2, No):
        if No % i == 0:
            return False
    return True

def main():
    Value = int(input("Enter a number: "))
    if prime(Value):
        print(f"{Value} is a prime number.")
    else:
        print(f"{Value} is not a prime number.")

if __name__ == "__main__":
    main()       