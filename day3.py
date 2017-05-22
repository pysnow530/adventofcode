#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd


def main():
    """入口"""
    data_frame = pd.read_table('day3.txt', delim_whitespace=True, header=None)

    nr_row_triangle = 0

    for row in data_frame.values:
        for idx in range(0, len(row), 3):
            a, b, c = row[idx:idx+3]

            nr_row_triangle += is_valid_triangle(a, b, c)

    print nr_row_triangle

    nr_column_triangle = 0

    for column in data_frame.T.values:

        for idx in range(0, len(column), 3):
            a, b, c = column[idx:idx+3]

            nr_column_triangle += is_valid_triangle(a, b, c)

    print nr_column_triangle


def is_valid_triangle(a, b, c):
    """判断三边是否可组成三角形
    判断依据：最短两边之和大于第三边
    假设 a <= b <= c
    只要 a + b > c 即可
    即   a + b + c > 2c
    即   (a + b + c) > (2 * max(a, b, c))
    """
    print type(a)
    max_side = max(a, b, c)
    is_valid = (a + b + c) > (2 * max_side)

    return is_valid


if __name__ == '__main__':
    main()
