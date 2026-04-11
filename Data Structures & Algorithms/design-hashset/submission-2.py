class MyHashSet:

    def __init__(self):
       self.mod = 1009
       self.store = [[] for _ in range(self.mod)]

    def add(self, key: int) -> None:
        bucket = self.store[key % self.mod]
        for k in bucket:
            if k == key:
                return
        bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.store[key % self.mod]
        for i, k in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                break

    def contains(self, key: int) -> bool:
        bucket = self.store[key % self.mod]
        for k in bucket:
            if k == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)