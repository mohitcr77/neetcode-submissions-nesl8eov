class LRUCache:

    def __init__(self, capacity: int):
         self.cache = {}
         self.cap = capacity

    def get(self, key: int) -> int:
        val = 0
        # add recently used val to end
        if key not in self.cache:
            return -1
        val = self.cache.pop(key)
        self.cache[key] = val
        return val
        

    def put(self, key: int, value: int) -> None:
        #remove 1st element which is the unsused val
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.cap:
            self.cache.pop(list(self.cache)[0])

        self.cache[key] = value
        print(f" put : {self.cache}")

        
