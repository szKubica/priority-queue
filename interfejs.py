from kolejka import *

if __name__ == '__main__':

    print("1.Add element")
    print("2.Delete element")
    print("3.Display queue")
    print("4.Display first element of queue")
    print("5.Exit")

    while True:
        wybor = input("Wybierz funkcję: ")

        if wybor == '1':
            elem, weight = input("Enter a number and after the space its weight to enter the queue: ").split()
            queue.add(elem, weight)

        if wybor == '2':
            queue.delete()

        if wybor == '3':
            queue.display()

        if wybor == '4':
            queue.first()

        if wybor == '5':
            break

        if int(wybor) not in range(1,6):
            print("Wybierz poprawny numer funkcji!")