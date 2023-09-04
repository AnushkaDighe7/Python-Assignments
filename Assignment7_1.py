import threading
def Even():
    data = range(2,21,2)
    for no in data:
        print("Even Numbers are : ",{no})

def Odd():
    data = range(1,20,2)
    for no in data:
        print("Odd Numbers are : ",{no})

def main():

    Even_thread = threading.Thread(target=Even)
    Odd_thread = threading.Thread(target=Odd)
   
    Even_thread.start()
    Odd_thread.start()
    
    Even_thread.join()
    Odd_thread.join()

if __name__ == "__main__":  
    main()  