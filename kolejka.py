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


queue1 = PriorityQueue()
queue2 = PriorityQueue()
queue3 = PriorityQueue()
queue4 = PriorityQueue()
queue5 = PriorityQueue()

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

if __name__ == '__main__':
    add_elements(queue1, 40)
    add_elements(queue1, 80)
    add_elements(queue2, 400)
    add_elements(queue2, 800)
    add_elements(queue3, 4000)
    add_elements(queue4, 8000)
    add_elements(queue3, 40000)
    add_elements(queue4, 80000)
