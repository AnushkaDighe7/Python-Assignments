import threading

def countsmallletters(string):
    thread_id = threading.get_ident()
    thread_name = threading.current_thread().name
    count = sum(1 for char in string if char.islower())
    print("Thread",thread_id)
    print(thread_name)
    print("Count of small letters  is : ",count) 

def countcapitalletters(string):
    thread_id = threading.get_ident()
    thread_name = threading.current_thread().name
    count = sum(1 for char in string if char.isupper())
    print("Thread",thread_id)
    print(thread_name)
    print("Count of Capital Letters is : ",count) 

def countdigits(string):
    thread_id = threading.get_ident()
    thread_name = threading.current_thread().name
    count = sum(1 for char in string if char.isdigit())
    print("Thread",thread_id)
    print(thread_name)
    print("Count of Digits is : ",count) 

def main():
    input_string = input("Enter a string: ")

    small_thread = threading.Thread(target=countsmallletters, args=(input_string,))
    capital_thread = threading.Thread(target=countcapitalletters, args=(input_string,))
    digits_thread = threading.Thread(target=countdigits, args=(input_string,))

    small_thread.start()
    small_thread.join()

    capital_thread.start()
    capital_thread.join()

    digits_thread.start()
    digits_thread.join()

if __name__ == "__main__":
    main()    