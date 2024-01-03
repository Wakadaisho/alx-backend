#!/usr/bin/python3

"""
MRU Caching
Most Recently Used (MRU) Cache
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU Cache
    """
    def __init__(self):
        """ Initialize MRU_Cache
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.queue.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            discard = self.queue.pop()
            self.cache_data.pop(discard)
            print("DISCARD: {}".format(discard))
        self.queue.append(key)
        self.cache_data.update({key: item})

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data.get(key)
        return None
