#!/usr/bin/env  python3



import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    The function should return a tuple of size two containing a
    start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination
    parameters.
    """
    start_index: int = 0
    end_index: int = 0
    if type(page) == int and type(page_size) == int:
        start_index = (page * page_size) - page_size
        end_index = page * page_size
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
            pass