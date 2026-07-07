"""
LRU CACHE
---------
Design a data structure that follows the constraints of a
Least Recently Used (LRU) cache.

Implement the LRUCache class:

- LRUCache(capacity)
- get(key)    -> returns value if present, else -1
- put(key, value)

When the cache exceeds its capacity, remove the least recently
used item.

Example:
capacity = 2

put(1,1)
put(2,2)
get(1)    -> 1
put(3,3)  -> evicts key 2
get(2)    -> -1
put(4,4)  -> evicts key 1
get(1)    -> -1
get(3)    -> 3
get(4)    -> 4
"""

from collections import OrderedDict
from typing import Optional


# ─────────────────────────────────────────────
# APPROACH 1 — BRUTE FORCE (List + Dictionary)
# ─────────────────────────────────────────────
"""
Store values in a dictionary and maintain usage order
using a list.

Every access requires removing and appending the key
inside the list.

Time
get : O(n)
put : O(n)

Space : O(capacity)
"""
class LRUCacheBrute:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        self.order.remove(key)
        self.order.append(key)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.order.remove(key)

        elif len(self.cache) == self.capacity:
            lru = self.order.pop(0)
            del self.cache[lru]

        self.cache[key] = value
        self.order.append(key)


# ─────────────────────────────────────────────
# APPROACH 2 — BETTER (OrderedDict)
# ─────────────────────────────────────────────
"""
Python's OrderedDict maintains insertion order.

Move recently used keys to the end.
Remove the first element when capacity is exceeded.

Time
get : O(1)
put : O(1)

Space : O(capacity)
"""
class LRUCacheBetter:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


# ─────────────────────────────────────────────
# APPROACH 3 — OPTIMAL (HashMap + Doubly Linked List)
# ─────────────────────────────────────────────
"""
Use

1. HashMap
   key -> node

2. Doubly Linked List
   Maintains usage order.

Most recently used node stays near the head.
Least recently used node stays near the tail.

Operations:
- get()    : Move node to front.
- put()    : Insert/update node at front.
- Remove tail when capacity is exceeded.

Time
get : O(1)
put : O(1)

Space : O(capacity)
"""


class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None


class LRUCacheOptimal:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.cache = {}

        self.left = Node()   # Most Recently Used side
        self.right = Node()  # Least Recently Used side

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node) -> None:

        prev = node.prev
        nxt = node.next

        assert prev is not None and nxt is not None
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node: Node) -> None:

        first = self.left.next
        assert first is not None

        self.left.next = node
        node.prev = self.left

        node.next = first
        first.prev = node

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:

            lru = self.right.prev
            assert lru is not None
            self.remove(lru)
            del self.cache[lru.key]


# ─────────────────────────────────────────────
# Test
# ─────────────────────────────────────────────
if __name__ == "__main__":

    def test(cache_class):

        cache = cache_class(2)

        cache.put(1, 1)
        cache.put(2, 2)

        print(cache.get(1))   # 1

        cache.put(3, 3)

        print(cache.get(2))   # -1

        cache.put(4, 4)

        print(cache.get(1))   # -1
        print(cache.get(3))   # 3
        print(cache.get(4))   # 4

    print("Brute Force")
    test(LRUCacheBrute)

    print("\nBetter")
    test(LRUCacheBetter)

    print("\nOptimal")
    test(LRUCacheOptimal)