from functools import wraps
import time
import random


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return str(self.queue)

    def add(self, elem, weight):
        try:
            steps = 0
            i=0
            while weight<=self.queue[i][1]:
                i += 1
                steps += 1
            self.queue.append(self.queue[len(self.queue)-1])
            steps += 1
            for j in range(len(self.queue),i,-1):
                self.queue[j-1] = self.queue[j-2]
                steps += 1
            self.queue[i]=[elem, weight]
            steps += 1
        except IndexError: 
            self.queue.append([elem, weight])
            steps += 1

        

    @timeit
    def delete(self):
        if len(self.queue) == 0:
            print("queue is empty")
        else:
            self.queue.pop(0)


    def display(self):
        if len(self.queue) ==0:
            print("queue is empty")
        else:
            print("[Element, weight]", queue)

    def first(self):
        if len(self.queue) == 0:
            print("queue is empty")
        else:
            print("First element:", self.queue[0][0])


queue = PriorityQueue()

@timeit
def add_elements(queue, volume):
    elements = []
    for i in range(1, volume+1):
        element = "elem_{}".format(i)
        weight = random.randint(1, volume)
        elements.append((element, weight))

    random.shuffle(elements)

    for element, weight in elements:
        queue.add(element, weight)

add_elements(queue, 10)
add_elements(queue, 100)
add_elements(queue, 4000)
add_elements(queue, 10000)

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