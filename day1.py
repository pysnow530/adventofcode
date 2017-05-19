#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

import numpy as np


def main():
    """入口，读取R3,L4类似的字符串数据，打印最后与原点的距离"""
    position = np.array((0, 0))
    direction = np.array((0, 1))

    items_str = raw_input('input data: ')
    items = items_str.split(', ')

    for item in items:
        turn, step = parse_item(item)
        direction = rotate(direction, turn)
        position += direction * step

    print math.fabs(position[0]) + math.fabs(position[1])


def parse_item(item):
    """解析R8形式的字符串，返回方向(左-1 右1)和步长8的元组"""
    turn_str, step_str = item[0], item[1:]
    turn = 1 if turn_str == 'R' else -1
    step = int(step_str)

    return turn, step


def rotate(direction, turn):
    """旋转一个方向，turn 左-1 右1"""
    dx, dy = direction
    new_direction = np.array((dy, -dx)) * turn

    return new_direction


if __name__ == '__main__':
    main()
