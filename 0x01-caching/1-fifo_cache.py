#!/usr/bin/env python3
"""
1. FIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    class that represents first input first output implementation for cache
    """
    def __init__(self):
        """
        instantiation method
        """
        super().__init__()

    def put(self, key, item):
        """
        method to add value to cache
        """
        if key is not None and item is not None:
            cache = self.cache_data
            if len(cache) >= BaseCaching.MAX_ITEMS and key not in cache.keys():
                first_key = list(self.cache_data.keys())[0]
                print(f"DISCARD: {first_key}")
                del self.cache_data[first_key]
            self.cache_data[key] = item

    def get(self, key):
        """
        retrieve an item by key
        """
        return self.cache_data.get(key, None)
