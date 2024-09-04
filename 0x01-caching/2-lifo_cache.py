#!/usr/bin/env python3
"""
2. LIFO Caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    class that represents last input first output implementation for cache
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
            if key in self.cache_data:
                self.cache_data.pop(key)
            elif len(self.cache_data) == BaseCaching.MAX_ITEMS:
                last_key, last_value = self.cache_data.popitem()
                print(f"DISCARD: {last_key}")
            self.cache_data[key] = item

    def get(self, key):
        """
        retrieve an item by key
        """
        if key is not None:
            return self.cache_data[key]
        return None
