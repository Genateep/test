# 2. На языке Python (2.7) реализовать минимум по 2 класса
# реализовывающих циклический буфер FIFO.
# Объяснить плюсы и минусы каждой реализации.
#
# Решение:
#     Первый вариант при заполнении изменяет объект класса и затем,
# при добавлении нового элемента, удаляет самый старый в списке.
#     Второй вариант при переполнении или опустошении возвращает ошибку,
# но имеет функцию возвращать элемент. Требует больше памяти, но быстрее,
# т.к. динамический массив может обращаться к элементу за O(1)


# Первая реализация:
# https://www.oreilly.com/library/view/python-cookbook/0596001673/ch05s19.html
class RingBuffer:
    """ class that implements a not-yet-full buffer """
    def __init__(self, size_max):
        self.max = size_max
        self.data = []

    class __Full:
        """ class that implements a full buffer """
        def append(self, x):
            """ Append an element overwriting the oldest one. """
            self.data[self.cur] = x
            self.cur = (self.cur + 1) % self.max

        def get(self):
            """ return list of elements in correct order """
            return self.data[self.cur:]+self.data[:self.cur]

    def append(self,x):
        """append an element at the end of the buffer"""
        self.data.append(x)
        if len(self.data) == self.max:
            self.cur = 0
            # Permanently change self's class from non-full to full
            self.__class__ = self.__Full

    def get(self):
        """ Return a list of elements from the oldest to the newest. """
        return self.data


# Вторая реализация:
class CyclesQueue:
    def __init__(self, size):
        self._items = [0] * size
        self._head = 0
        self._tail = 0

        self._count = 0
        self._size = size

    def push(self, el):
        if self.full():
            raise Exception("Queue is full!")

        self._items[self._head] = el

        self._count += 1
        self._head = self.next_index(self._head)

    def pop(self):
        if self.empty():
            raise Exception("Queue is empty!")

        item = self._items[self._tail]

        self._count -= 1

        self._tail = self.next_index(self._tail)
        return item

    def count(self):
        return self._count

    def size(self):
        return self._size

    def full(self):
        return self._count == self._size

    def empty(self):
        return self._count == 0

    def next_index(self, index):
        temp = index + 1
        if temp >= self._size:
            temp = 0
        return temp
