#!/usr/bin/env python3
"""
Hypermedia pagination
"""
import csv
import math
from typing import List, Tuple, Dict, Union, Any, Optional


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
     return a tuple of size two containing a start index and an end index
     corresponding to the range of indexes to return in a list for those
     particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
         takes two integer arguments page with default value 1 and page_size
         with default value 10.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        data_set = self.dataset()
        start_index, end_index = index_range(page, page_size)
        if start_index > len(data_set):
            return []
        return data_set[start_index:end_index]

    def get_hyper(
            self,
            page: int = 1,
            page_size: int = 10
            ) -> Dict[str, Union[int, List[List[Any]], Optional[int]]]:
        """
        returns a dictionary containing the following key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        try:
            dataset = self.get_page(page, page_size)
            total_items = len(self.__dataset)
            total_pages = (total_items + page_size - 1) // page_size
            if page >= 1 and page < total_pages:
                next_page = page + 1
            else:
                next_page = None

            if page == 1:
                prev_page = None
            else:
                prev_page = page - 1

            return {
                    'page_size': page_size,
                    'page': page,
                    'data': dataset,
                    'next_page': next_page,
                    'prev_page': prev_page,
                    'total_pages': total_pages
                    }
        except AssertionError:
            return {
                    'page_size': 0,
                    'page': page,
                    'data': [],
                    'next_page': None,
                    'prev_page': None,
                    'total_pages': 0
                    }
