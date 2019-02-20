#!/usr/bin/env python
# coding: utf8


class Solution:

    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':

        def do(x0, y0, x1, y1):
            result = []
            if x0 > x1 or y0 > y1:
                return result
            elif (x0, y0) == (x1, y1):
                return [matrix[x0][y0]]
            result += matrix[x0][y0:y1]
            result += [matrix[i][y1] for i in range(x0, x1+1)]
            if x0 != x1:
                result += matrix[x1][y0+1:y1][::-1]
            if y0 != y1:
                result += [matrix[i][y0] for i in range(x0+1, x1+1)][::-1]
            result += do(x0+1, y0+1, x1-1, y1-1)
            return result

        if matrix == []:
            return []
        return do(0, 0, len(matrix)-1, len(matrix[0])-1)
