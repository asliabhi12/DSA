
from queue import PriorityQueue


class PriorityQu(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # check queue is empty

    def isEmpty(self):
        return len(self.queue) == 0


    def insert(self, data):
        self.queue.append(data)

    def delete(self):
        try:
            max_value = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max_value]:
                    max_value = i

            item = self.queue[max_value]
            del self.queue[max_value]
            return item
        except IndexError:
            print()
            exit()

pq = PriorityQu()

pq.insert(3)
pq.insert(4)
pq.insert(5)
pq.insert(1)

print(pq.isEmpty())

print(pq)

print(pq.delete())

print(pq)

