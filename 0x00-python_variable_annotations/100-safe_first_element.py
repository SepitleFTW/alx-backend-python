#!/usr/bin/env python3
'''add cool comment
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''add cool comment
    '''
    if lst:
        return lst[0]
    else:
        return None
