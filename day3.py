#!/usr/bin/env python
# -*- coding: utf-8 -*-
def main():
    """入口"""
    nr_triangle = 0

    for line in open('day3.txt'):
        line = line.strip()
        a, b, c = line.split()
        a, b, c = int(a), int(b), int(c)

        if is_valid_triangle(a, b, c):
            nr_triangle += 1

    print nr_triangle


def is_valid_triangle(a, b, c):
    """判断三边是否可组成三角形
    判断依据：最短两边之和大于第三边
    假设 a <= b <= c
    只要 a + b > c 即可
    即   a + b + c > 2c
    即   (a + b + c) > (2 * max(a, b, c))
    """
    max_side = max(a, b, c)

    return (a + b + c) > (2 * max_side)


if __name__ == '__main__':
    main()
