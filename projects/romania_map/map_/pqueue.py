import heapq
from typing import Any

class PriorityQueue(list):

    def __init__(self, iterable: list = list()) -> None:
        self.pqueue: list = iterable
        heapq.heapify(self.pqueue)

    def pop(self): return heapq.heappop(self.pqueue)
    def put(self, item: Any): return heapq.heappush(self.pqueue, item)


    def __getitem__(self, item: Any):
        for elem in self.pqueue:
            if elem == item:
                return elem

    def __len__(self): return self.pqueue.__len__()
    
    def remove(self, __value: Any) -> None:
        self.pqueue.remove(__value)
        heapq.heapify(self.pqueue)

    def __repr__(self) -> str:
        return self.pqueue.__repr__()