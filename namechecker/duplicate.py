class RemoveDuplicate:
    def __init__(self, arr):
        self.arr = arr
#        self.n = n

    def removeDuplicate(self):
        seen = set()
        result = []
        for char in self.arr:
            if char not in seen:
                seen.add(char)
                result.append(char)
        return result
