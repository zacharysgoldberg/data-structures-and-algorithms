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

    def max_heapify(self, heap, index):
        left = index * 2 + 1
        right = index * 2 + 2
        largest = index
        if left < len(heap) and heap[left] > heap[largest]:
            largest = left
        if right < len(heap) and heap[right] > heap[largest]:
            largest = right
        if largest != index:
            heap[index], heap[largest] = heap[largest], heap[index]
            self.max_heapify(self.heap, largest)

    def build_heap(self, lst):
        self.heap = lst
        for i in range(len(lst) - 1, -1, -1):
            self.min_heapify(self.heap, i)


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, data):
        self.heap.append(data)
        self._percolate_up(len(self.heap) - 1)

    def get_max(self):
        if self.heap:
            return self.heap[0]
        return None

    def pop_max(self):
        if len(self.heap) > 1:
            max = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]
            self.max_heapify(self.heap, 0)
            return max
        elif len(self.heap) == 1:
            max = self.heap[0]
            del self.heap[0]
            return max
        else:
            return None

    def _percolate_up(self, index):
        parent = (index - 1) // 2
        if index <= 0:
            return
        elif self.heap[parent] < self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._percolate_up(parent)

    def convert_to_max(self, min_heap):
        # middle to first indices contain all parent nodes
        for i in range(len(min_heap) // 2, -1, -1):
            self.max_heapify(min_heap, i)
        return min_heap

    def max_heapify(self, heap, index):
        left = index * 2 + 1
        right = index * 2 + 2
        largest = index
        if left < len(heap) and heap[left] > heap[largest]:
            largest = left
        if right < len(heap) and heap[right] > heap[largest]:
            largest = right
        if largest != index:
            heap[index], heap[largest] = heap[largest], heap[index]
            self.max_heapify(self.heap, largest)

    def buildHeap(self, lst):
        self.heap = lst
        for i in range(len(lst) - 1, -1, -1):
            self.max_heapify(self.heap, 0)


def find_k_smallest(lst, k):
    heap = MinHeap()
    heap.build_heap(lst)
    ksmallest = [heap.pop_min() for _ in range(k)]
    return ksmallest


def find_k_Largest(lst, k):
    heap = MaxHeap()
    heap.buildHeap(lst)
    klargest = [heap.pop_max() for _ in range(k)]
    return klargest


class SlidingWindowMedian:
    def __init__(self):
        self.max_heaps = []
        self.min_heaps = []

    def find_sliding_window_median(self, nums, k):
        result = []
        for i in range(len(nums)):
            if not self.max_heaps or nums[i] <= -self.max_heaps[0]:
                heappush(self.max_heaps, -nums[i])
            else:
                heappush(self.min_heaps, nums[i])
            self.rebalance_heaps()
            # if we have at least 'k' elements in the sliding window
            if i - k + 1 >= 0:
                # if k is even
                if k % 2 == 0:
                    med = (-self.max_heaps[0] + self.min_heaps[0]) / 2
                    result.append(med)
                # if k is odd
                else:
                    med = float(-self.max_heaps[0])
                    result.append(med)
                # remove the element going out of the sliding window
                heap = nums[i - k + 1]
                if heap <= -self.max_heaps[0]:
                    self.remove_heap(self.max_heaps, -heap)
                else:
                    self.remove_heap(self.min_heaps, heap)
                self.rebalance_heaps()
        return result

        """
        either both the heaps will have equal number of elements
        or max-heap will have one more element than the min-heap
        """

    def rebalance_heaps(self):
        if len(self.max_heaps) > len(self.min_heaps) + 1:
            heappush(self.min_heaps, -heappop(self.max_heaps))
        elif len(self.max_heaps) < len(self.min_heaps):
            heappush(self.max_heaps, -heappop(self.min_heaps))

    def remove_heap(self, heap_list, heap):
        index = heap_list.index(heap)
        # delete element from list
        del heap_list[index]


# Find the Median of a Number Stream (Heap Queues)


class MedianStream:
    def __init__(self):
        self.max_heaps = []
        self.min_heaps = []

    def insert_num(self, num):
        if not self.max_heaps or num <= -self.max_heaps[0]:
            # use negative value for max heap because heappop removes and returns the lowest heap value in a list
            heappush(self.max_heaps, -num)
        else:
            heappush(self.min_heaps, num)
        self.rebalance_heaps()

    def find_median(self):
        if len(self.max_heaps) == len(self.min_heaps):
            med = (-self.max_heaps[0] + self.min_heaps[0]) / 2
            return med
        return float(-self.max_heaps[0])

    def rebalance_heaps(self):
        if len(self.max_heaps) > len(self.min_heaps) + 1:
            heappush(self.min_heaps, -heappop(self.max_heaps))
        elif len(self.max_heaps) < len(self.min_heaps):
            heappush(self.max_heaps, -heappop(self.min_heaps))

    # Maximize Capital
    def find_maximum_capital(self, capital, profits, number_of_projects, initial_capital):
        # insert all project capitals to a min-heap
        for i in range(len(profits)):
            heappush(self.min_heaps, (capital[i], i))
        # find projects that can be selected within available capital and insert them in a max-heap
        for _ in range(number_of_projects):
            while self.min_heaps and self.min_heaps[0][0] <= initial_capital:
                capital, i = heappop(self.min_heaps)
                heappush(self.max_heaps, -profits[i])
            if not self.max_heaps:
                break
            # select the project with the maximum profit
            initial_capital += -self.max_heaps[0]

        return initial_capital


if __name__ == "__main__":
    # lst = [9, 4, 7, 1, -2, 6, 5]
    # k = 3
    # print(find_k_smallest(lst, k))

    # lst = [9, 4, 7, 1, -2, 6, 5]
    # k = 3
    # print(find_k_Largest(lst, k))

    # heap = MedianStream()
    # lst = [1, 2, -1, 3, 5]
    # for i in lst:
    #     heap.insert_num(i)
    # print(heap.max_heaps, heap.min_heaps)
