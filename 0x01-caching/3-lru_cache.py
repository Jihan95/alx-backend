#!/usr/bin/env python3
"""
3. LRU Caching
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    class that represents last input first output implementation for cache
    """
    def __init__(self):
        """
        instantiation method
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        method to add value to cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.pop(key)

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """
        retrieve an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        item = self.cache_data.pop(key)
        self.cache_data[key] = item
        return item
