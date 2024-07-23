#!/usr/bin/env python3
"""
Contains definition of index_range helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Takes 2 integer arguments and returns a tuple of size two
    containing the start and end index corresponding to the range of
    indexes to return in a list for those pagination parameters.

    Args:
        page (int): page number to return (pages are 1-indexed)
        page_size (int): number of items per page

    Returns:
        Tuple[int, int]: A tuple containing the start index (inclusive) and
        end index (exclusive) for the given page and page size.
    """
    if page < 1:
        raise ValueError("Page number must be greater than or equal to 1.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index

