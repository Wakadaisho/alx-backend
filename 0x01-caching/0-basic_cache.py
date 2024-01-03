#!/usr/bin/python3
""" BaseCache module
Store and retirieve values in a rudimentary cache
implemented using a dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic Cache
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
        self.cache_data.update({key: item})

    def get(self, key):
        """Get value from cache

        Args:
            key(str): dictionary key in cache
        """
        return self.cache_data.get(key)
