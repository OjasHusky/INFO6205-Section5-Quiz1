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
        key = array[i]
        t= i-1
        while i> = 0 and key < array[t]:
            self.swap(i, i + 1)
            t=t-1
        array[t+1] = key



