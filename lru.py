"""LRU Cache implementation in python."""
from collections import OrderedDict


class LRUCache(OrderedDict):
    def __init__(self, capacity, *args, **kwds):
        """Initialize the cache.

        :type capacity: int
        """
        super().__init__(*args, **kwds)
        self.capacity = capacity

    def __setitem__(self, key, value, **kwargs):
        if key in self:
            del self[key]
        OrderedDict.__setitem__(self, key, value)

    def __getitem__(self, key):
        value = OrderedDict.__getitem__(self, key)
        self.__setitem__(key, value)
        return value

    def get(self, key, default=-1):
        """Get a given key from the cache.

        :type key: int
        :type default: int
        :rtype: int
        """
        if key not in self:
            return default
        return self[key]

    def put(self, key, value):
        """Put a key to the cache.

        :type key: int
        :type value: int
        :rtype: void
        """
        if len(self) >= self.capacity and \
           key not in self:
            self.popitem(last=False)
        self[key] = value
