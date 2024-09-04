#!/usr/bin/env python3
"""
BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache definition
    """

    MAX_ITEMS = float('inf')

    def __init__(self):
        """
        instantiation method
        """
        super().__init__()

    def put(self, key, item):
        """
        adding a value to cache_data
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        retrieve data from cache if exists
        """
        if key in self.cache_data.keys():
            return self.cache_data[key]
        return None
