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
        key = self.array[i]
        t= i-1
        while t>= 0 and key < self.array[t]:
            self.swap(t, t + 1)
            t=t-1
        self.array[t + 1] = key



