from heapq import *


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, data):
        self.heap.append(data)
        self._percolate_up(len(self.heap) - 1)

    def get_min(self):
        if self.heap:
            return self.heap[0]
        return None

    def pop_min(self):
        if len(self.heap) > 1:
            min = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.min_heapify(self.heap, 0)
            return min
        elif len(self.heap) == 1:
            min = self.heap[0]
            del self.heap[0]
            return min
        else:
            return None

    def _percolate_up(self, index):
        parent = (index - 1) // 2
        if index <= 0:
            return
        elif self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._percolate_up(parent)
        # Convert Max-Heap to Min-Heap

    def convert_to_min(self, max_heap):
        # middle to first indices contain all parent nodes
        for i in range(len(max_heap) // 2, -1, -1):
            self.min_heapify(max_heap, i)
        return max_heap

    def min_heapify(self, heap, index):
        left = index * 2 + 1
        right = index * 2 + 2
        smallest = index
        if left < len(heap) and heap[left] < heap[smallest]:
            smallest = left
        if right < len(heap) and heap[right] < heap[smallest]:
            smallest = right
        if smallest != index:   # check if current index is not the smallest
            # swap current index with the smallest
            heap[index], heap[smallest] = heap[smallest], heap[index]
            self.min_heapify(heap, smallest)

    def build_heap(self, lst):
        self.heap = lst
        for i in range(len(lst) - 1, -1, -1):
            self.min_heapify(self.heap, i)


def find_k_smallest(lst, k):
    heap = MinHeap()
    heap.build_heap(lst)
    ksmallest = [heap.pop_min() for _ in range(k)]
    return ksmallest


if __name__ == "__main__":
    # lst = [9, 4, 7, 1, -2, 6, 5]
    # k = 3
    # print(find_k_smallest(lst, k))
