class MyHashMap:
    def __init__(self):
        self.MOD = 1009
        # list of buckets of key-value tuples
        self.store = [[] for _ in range(self.MOD)]

    def put(self, key: int, value: int) -> None:
        bucket = self.store[key % self.MOD]
        tup = (key, value)
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = tup
                return
        bucket.append(tup)

    def get(self, key: int) -> int:
        bucket = self.store[key % self.MOD]
        for (k, v) in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        bucket = self.store[key % self.MOD]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)