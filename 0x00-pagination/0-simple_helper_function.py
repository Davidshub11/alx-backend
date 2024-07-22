#!/usr/bin/env python3

def index_range(page: int, page_size: int) -> tuple[int, int]:
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index - 1  #end_index - 1 because end_index is exclusive in Python ranges

