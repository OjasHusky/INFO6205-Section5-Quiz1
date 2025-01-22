from typing import List


class InsertionSort:
    def __init__(self, array):
        self.array = array

    def sort(self) -> List:
        """Sorts the array using Insertion Sort."""
        for i in range(1, len(self.array)):
            self.insert(i)
        return self.array

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def insert(self, i):
        """Inserts the 'Transition element' into its correct position in the sorted portion of the array."""
        for ele in range(1,len(i)):
        key = i[ele]
        t= ele-1
        while ele> = 0 and key<i[t]:
            self.swap(ele, ele + 1)
            ele = ele-1
        ele[t+1] = key


