#!/usr/bin/python3
""" FIFOCache module
Store and retirieve values in a rudimentary cache
implemented using a dictionary
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Cache
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
            discard = list(self.cache_data.keys())[0]
            self.cache_data.pop(discard)
            print("DISCARD: {}".format(discard))

        self.cache_data.update({key: item})

    def get(self, key):
        """Get value from cache

        Args:
            key(str): dictionary key in cache
        """
        return self.cache_data.get(key)
