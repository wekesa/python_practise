# LRU (Least Recently Used) Cache discards the least recently used items first.
# This algorithm requires keeping track of what was used when, which is expensive
# if one wants to make sure the algorithm always discards the least recently used item.
# General implementations of this technique require keeping “age bits” for cache-lines
# and track the “Least Recently Used” cache-line based on age-bits.
# This solution uses OrderedDict from collections package/module
# Operations supported

# * get(key) – Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# * put(key, value) – Set or insert the value if the key is not already present. When the cache reached its capacity,
# it should invalidate the least recently used item before inserting a new item.
#
# The cache is always initialized with positive capacity.

from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


if __name__ == '__main__':
    cache = LRUCache(3)
    cache.put(1, 1)
    print(cache.cache)
    cache.put(2, 2)
    cache.put(3, 3)
    print(cache.cache)
    cache.get(3)
    cache.put(4, 4)
    print(cache.cache)

# Time Complexity O(1)
