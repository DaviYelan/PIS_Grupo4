class ShellSort:
    
    def shell_sort(self, array, key, ascending):
        n = len(array)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = array[i]
                j = i
                if ascending:
                    while j >= gap and key(array[j - gap]) > key(temp):
                        array[j] = array[j - gap]
                        j -= gap
                else:
                    while j >= gap and key(array[j - gap]) < key(temp):
                        array[j] = array[j - gap]
                        j -= gap
                array[j] = temp
            gap //= 2
        return array

    def sort_primitive_ascendent(self, array):
        return self.shell_sort(array, key=lambda x: x, ascending=True)

    def sort_primitive_descendent(self, array):
        return self.shell_sort(array, key=lambda x: x, ascending=False)
    
    def sort_shell_attribute_ascendent(self, array, attribute):
        key = lambda obj: getattr(obj, attribute)
        return self.shell_sort(array, key=key, ascending=True)

    def sort_shell_attribute_descendent(self, array, attribute):
        key = lambda obj: getattr(obj, attribute)
        return self.shell_sort(array, key=key, ascending=False)
