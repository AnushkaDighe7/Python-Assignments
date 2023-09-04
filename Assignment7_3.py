import threading

def evenlist(numbers):

    Sum = sum(No for No in numbers if No % 2 == 0)
    print("Sum of even elements: ",Sum)


def oddlist(numbers):
    Sum = sum(No for No in numbers if No % 2 != 0)
    print("Sum of odd elements: ", Sum)


def Input():
    List = []
    print("Enter number of elements : ")
    Size = int(input())

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        List.append(Value)
    return List

List = Input()
def main():
    even_thread = threading.Thread(target=evenlist, args=(List,))
    odd_thread = threading.Thread(target=oddlist, args=(List,))

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()
if __name__ == "__main__":
    main() 