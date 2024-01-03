#!/usr/bin/python3
""" LIFOCache module
Store and retirieve values in a rudimentary cache
implemented using a dictionary
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Cache
    Cache values in a dictionary
    """
    def put(self, key, item):
        """Store in cache

        Args:
            key(str): dictionary key in cache
            value(any): value stored in dictionary
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.pop(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            discard, _ = self.cache_data.popitem()
            print("DISCARD: {}".format(discard))

        self.cache_data.update({key: item})

    def get(self, key):
        """Get value from cache

        Args:
            key(str): dictionary key in cache
        """
        return self.cache_data.get(key)
