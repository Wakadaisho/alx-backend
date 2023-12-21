#!/usr/bin/env python3
"""
Get index range based on page and page_size
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Get index range based on page and page_size"""
    start: int = (page - 1) * page_size
    end: int = start + page_size
    return (start, end)
