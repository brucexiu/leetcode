#!/usr/bin/env python
# coding: utf8


class Solution:
    def findRestaurant(self, list1: 'List[str]', list2: 'List[str]') -> 'List[str]':
        common_interest_dict = {}
        min_common_interest = 10000
        result = []
        for i, c in enumerate(list1):
            common_interest_dict[c] = i
        for i, c in enumerate(list2):
            if i > min_common_interest:
                break
            else:
                min_index = common_interest_dict.get(c, min_common_interest) + i
                if min_index < min_common_interest:
                    result = [c]
                    min_common_interest = min_index
                elif min_index == min_common_interest:
                    result.append(c)
        return result
