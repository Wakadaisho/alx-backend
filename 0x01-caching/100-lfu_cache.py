#!/usr/bin/python3

"""
LFU Caching
Least Frequently Used (LFU) Cache
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU Cache
    """

    def __init__(self):
        """ Initialize LFU_Cache
        """
        super().__init__()
        self.queue = []
        self.count = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.queue.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            max_count = -1
            max_count_keys = []
            discard = None
            for k, v in self.count.items():
                if v > max_count:
                    max_count = v
                    max_count_keys.clear()
                    max_count_keys.append(k)
                elif v == max_count:
                    max_count_keys.append(k)
            if len(max_count_keys) == 1:
                discard = max_count_keys[0]
            else:
                for k in self.queue:
                    if k in max_count_keys:
                        discard = k
                        break
            self.queue.remove(discard)
            self.cache_data.pop(discard)
            self.count.pop(discard)
            print("DISCARD: {}".format(discard))
        self.queue.append(key)
        self.cache_data.update({key: item})
        self.count.update({key: 0})

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.count[key] += 1
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data.get(key)
        return None
