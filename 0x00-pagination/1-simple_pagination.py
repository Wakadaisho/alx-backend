#!/usr/bin/env python3
"""
Class to paginate a database of popular baby names.
"""

import csv
import math
from typing import List


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
        """Get index range based on page and page_size"""
        start: int = (page - 1) * page_size
        end: int = start + page_size

        if not (isinstance(page, int) and isinstance(page_size, int)):
            raise AssertionError

        if (page <= 0 or page_size <= 0):
            raise AssertionError

        return self.dataset()[start:end]
