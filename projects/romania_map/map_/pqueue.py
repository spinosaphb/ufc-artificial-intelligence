from dataclasses import dataclass
import heapq
from typing import Any, Callable, Iterator, List, TypeVar

class PriorityQueue(list):
    _T = TypeVar("_T")
    def __init__(self, list_: List[_T], priority_fn: Callable = None) -> None:
        if priority_fn: PriorityObject.set_priority_fn(priority_fn)
        self.pqueue: list = [PriorityObject(elem) for elem in list_]
        heapq.heapify(self.pqueue)

    def pop(self) -> _T: 
        po: PriorityObject = heapq.heappop(self.pqueue)
        return po.d

    def put(self, item: Any):
        po = PriorityObject(item)
        return heapq.heappush(self.pqueue, po)

    def __getitem__(self, item: Any):
        for elem in self.pqueue:
            if elem == item:
                return elem

    def __len__(self): return self.pqueue.__len__()
    
    def remove(self, __value: Any) -> None:
        po = PriorityObject(__value)
        self.pqueue.remove(po)
        heapq.heapify(self.pqueue)

    def __repr__(self) -> str:
        return self.pqueue.__repr__()

    def __iter__(self) -> Iterator[_T]:
        return super().__iter__()


class PriorityObject:
    __priority_fn: Callable = lambda x:x

    def __init__(self, data: TypeVar("_T")) -> None:
        self._data = data

    @classmethod
    def set_priority_fn(cls, p_fn) -> None:
        cls.__priority_fn = p_fn

    @property
    def d(self): return self._data

    def __lt__(self, __o: 'PriorityObject'):
        return PriorityObject.__priority_fn(self._data) < \
        PriorityObject.__priority_fn(__o._data)

    def __eq__(self, __o: 'PriorityObject') -> bool:
        return self._data == __o._data



    
