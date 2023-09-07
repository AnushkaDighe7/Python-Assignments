import threading

def get_input():
    Data = []
    
    num = int(input("Enter the Number : "))
    Data.append(num)
        
    return Data

Data = get_input()

def calculate_factors(thread_name, numbers, factor_sum_function):
    
    for num in numbers:
        factors_sum = factor_sum_function(num)
        print(thread_name)
        print(" Addition of Factors is : ",factors_sum)
    
def even_factors_sum(number):
    factors = [i for i in range(1, number + 1) if number % i == 0 and i % 2 == 0]
    return sum(factors)

def odd_factors_sum(number):
    factors = [i for i in range(1, number + 1) if number % i == 0 and i % 2 != 0]
    return sum(factors)

def main():

    even_factors_thread = threading.Thread(target=lambda: calculate_factors("Even thread", Data, even_factors_sum))
    odd_factors_thread = threading.Thread(target=lambda: calculate_factors("Odd thread", Data, odd_factors_sum))

    even_factors_thread.start()
    even_factors_thread.join()

    odd_factors_thread.start()
    odd_factors_thread.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
