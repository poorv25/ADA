class Heap:
    def __init__(self):
        self.heap_list = [0]
        self.size = 0

    def insert(self, item):
        self.heap_list.append(item)
        self.size += 1
        self.percolate_up(self.size)

    def percolate_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i //= 2

    def delete_min(self):
        min_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.size -= 1
        self.heap_list.pop()
        self.percolate_down(1)
        return min_val

    def percolate_down(self, i):
        while (i * 2) <= self.size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i):
        if (i * 2 + 1) > self.size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1


def heap_sort(lst):
    heap = Heap()
    sorted_lst = []
    for num in lst:
        heap.insert(num)
    while heap.size > 0:
        sorted_lst.append(heap.delete_min())
    return sorted_lst
