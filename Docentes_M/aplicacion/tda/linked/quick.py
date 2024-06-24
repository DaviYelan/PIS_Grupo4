class QuickSort:
    
    def partition(self, array, low, high, key, ascending):
        pivot = key(array[high])
        i = low - 1
        for j in range(low, high):
            if (ascending and key(array[j]) <= pivot) or (not ascending and key(array[j]) >= pivot):
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    def quick_sort(self, array, low, high, key, ascending):
        if low < high:
            pi = self.partition(array, low, high, key, ascending)
            self.quick_sort(array, low, pi - 1, key, ascending)
            self.quick_sort(array, pi + 1, high, key, ascending)

    def sort_primitive_ascendent(self, array):
        self.quick_sort(array, 0, len(array) - 1, key=lambda x: x, ascending=True)
        return array

    def sort_primitive_descendent(self, array):
        self.quick_sort(array, 0, len(array) - 1, key=lambda x: x, ascending=False)
        return array
    
    def sort_quick_attribute_ascendent(self, array, attribute):
        key = lambda obj: getattr(obj, attribute)
        self.quick_sort(array, 0, len(array) - 1, key=key, ascending=True)
        return array

    def sort_quick_attribute_descendent(self, array, attribute):
        key = lambda obj: getattr(obj, attribute)
        self.quick_sort(array, 0, len(array) - 1, key=key, ascending=False)
        return array
