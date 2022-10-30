from datetime import datetime
from random import randint, seed

# Инициализирует генератор случайных чисел.
seed(1, 1) # seed=1 version=1

# Класс указателя для очереди.
class Node:
    def __init__(self, data): # O(1)
        global N_op
        self.data = data # Данные указателя. # O(1)
        N_op += 1
        self.next = None # Ссылка на следующий указатель. # O(1)
        N_op += 1

# Класс очереди с указателями.
class Queue:
    def __init__(self): # O(1)
        global N_op
        self.head = None # Голова очереди. # O(1)
        N_op += 1
        self.len = 0 # Длина очереди. # O(1)
        N_op += 1

    def enqueue(self, data): # O(self.len)
        global N_op
        temp = Node(data) # O(1)
        N_op += 1
        if self.head is None: # O(1)
            N_op += 1
            self.head = temp # O(1)
            N_op += 1
        else: # O(1)
            N_op += 1
            for i in self: # O(self.len)
                if i.next is None: # O(1)
                    N_op += 1
                    break
            i.next = temp # O(1)
            N_op += 1
        self.len += 1 # O(1) O(1)
        N_op += 2

    def dequeue(self): # O(1)
        global N_op
        if self.len >= 1: # O(1)
            N_op += 1
            temp, self.head = self.head, self.head.next # O(1) O(1)
            N_op += 2
            self.len -= 1 # O(1) O(1)
            N_op += 2
            return temp.data # O(1)
            N_op += 1
        N_op += 1
        return None # O(1)

    def getByIndex(self, index): # O(self.len)
        global N_op
        if index >= self.len: # O(1)
            N_op += 2
            return None # O(1)
        for i in range(self.len-self.len+index): # O(self.len-self.len+index)
            N_op += 1
            self.enqueue(self.dequeue())
        res = self.dequeue() # O(1)
        N_op += 1
        for i in range(self.len-index): # O(self.len-index)
            N_op += 1
            self.enqueue(self.dequeue())
        N_op += 1
        return res # O(1)

    def peekByIndex(self, index): # O(self.len)
        global N_op
        if index >= self.len: # O(1)
            N_op += 2
            return None # O(1)
        res = None # O(1)
        N_op += 1
        for i in range(self.len): # O(self.len)
            if i == index: # O(1)
                N_op += 1
                res = self.head.data # O(1)
                N_op += 1
            self.enqueue(self.dequeue())
        N_op += 1
        return res # O(1)

    def setByIndex(self, index, data): # O(self.len)
        global N_op
        if index >= self.len: # O(1)
            N_op += 2
            return None # O(1)
        for i in range(self.len-self.len+index): # O(self.len-self.len+index)
            N_op += 1
            self.enqueue(self.dequeue())
        self.enqueue(data)
        for i in range(self.len-index-1): # O(self.len-index-1)
            N_op += 1
            self.enqueue(self.dequeue())

    def swap(self, index1, index2): # O(1)
        global N_op
        elem1 = self.getByIndex(index1) # O(1)
        N_op += 1
        if index2 > index1: # O(1)
            N_op += 1
            elem2 = self.getByIndex(index2-1) # O(1)
            N_op += 2
        else: # O(1)
            N_op += 1
            elem2 = self.getByIndex(index2) # O(1)
            N_op += 1

        if index1 > index2: # O(1)
            N_op += 1
            self.setByIndex(index2, elem1)
            if index1 >= self.len: # O(1)
                N_op += 1
                self.enqueue(elem2)
            else: # O(1)
                N_op += 1
                self.setByIndex(index1, elem2)
        else: # O(1)
            N_op += 1
            self.setByIndex(index1, elem2)
            if index2 >= self.len: # O(1)
                N_op += 1
                self.enqueue(elem1)
            else: # O(1)
                N_op += 1
                self.setByIndex(index2, elem1)

    def __iter__(self): # O(self.len)
        global N_op
        node = self.head # O(1)
        N_op += 1
        while node is not None: # O(self.len)
            N_op += 2
            yield node # O(1)
            node = node.next # O(1)
            N_op += 1

    def __len__(self): # O(1)
        global N_op
        N_op += 1
        return self.len # O(1)

    def __str__(self):
        res = ""
        flag = True
        for i in self:
            if i.next is None:
                res += f"{i.data}"
            elif flag:
                res += f"{i.data} -> ... -> "
                flag = False
        return res

# Метод для постройки max-heap путем сравнения родителей
# и левых детей.

def heapify(q, length): # O(length)
    global N_op
    for i in range(length): # O(length)
        # Если ребенок больше родителя
        # завести индекс ребенка.
        if q.peekByIndex(i) > q.peekByIndex(int((i-1)/2)): # O(3)
            N_op += 3
            largest = i # O(1)
            N_op += 1
            # Пока дети меньше родителей
            # менять местами индексы и
            # родителей с детьми в очереди.
            while q.peekByIndex(largest) > q.peekByIndex(int((largest-1)/2)):
                N_op += 3
                q.swap(largest, int((largest-1)/2)) # O(2)
                N_op += 2
                largest = int((largest-1)/2) # O(3)
                N_op += 3

# Метод сортировки очереди.

def heapSort(q, length):
    global N_op
    # Построение max-heap.
    heapify(q, length)
    # Проход по массиву, не учитывая последние,
    # отсортированные элементы.
    for i in range(length-1, 0, -1):
        # Меняем местами первый и последний,
        # рассматриваемый элемент очереди.
        # Заводим индексы родителя и ребенка.
        q.swap(0, i)
        parent, child = 0, 0
        N_op += 2
        # Проверяем детей на то, кто больше родителя, и
        # меняем их местами, убеждаясь, что индексы детей
        # не больше рассматриваемой длины очереди.
        # Повторяем действия, пока
        # есть дети больше родителя.
        while True:
            child = 2 * parent + 1
            N_op += 1
            if child < (i-1) and q.peekByIndex(child + 1) > q.peekByIndex(child):
                N_op += 5
                child += 1
                N_op += 2
            if child < i and q.peekByIndex(child) > q.peekByIndex(parent):
                N_op += 3
                q.swap(parent, child)
            parent = child
            N_op += 1
            if child >= i:
                N_op += 1
                break

# Метод генерации очереди.

def generate(n):
    q = Queue()
    for _ in range(n):
        q.enqueue(randint(0, 100))
    return q

def main(q):
    heapSort(q, len(q))

N_op = 0

if __name__ == "__main__":
    for n in range(50, 501, 50):
        q = generate(n)

        start_time = datetime.now()
        main(q)
        end_time = datetime.now()
        delta = end_time - start_time

        print(f"\tТест {n//50}.\nКол-во входных данных: {n}\nF(n): 'calculates with hand'\nN_op: {N_op}\nO(f(n)): 'O big'\nВремя выполения: {round(delta.total_seconds()*1000, 5)} ms\nРезультата сортировки: {q}")
        if n >= 200:
            break



