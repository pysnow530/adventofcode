#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import numpy as np


def main():
    """入口"""
    current_position = np.array((0, 0))

    instructions = open('day2.txt').readlines()

    for instruction in instructions:
        instruction = instruction.strip()

        for direction_char in instruction:
            direction = translate_char_to_direction(direction_char)
            current_position += direction
            current_position = correct_position(current_position)

        print translate_position_to_button_number(current_position)


def translate_char_to_direction(direction_char):
    """将字符转换为方向向量"""
    direction_map = {
        'L': np.array((-1, 0)),
        'R': np.array(( 1,  0)),
        'U': np.array(( 0,  1)),
        'D': np.array(( 0, -1)),
    }

    return direction_map[direction_char]


def correct_position(position):
    """如果超出范围，修正位置"""
    correction_map = {-2: -1, 2: 1}

    x, y = position
    if x in correction_map:
        x = correction_map[x]
    if y in correction_map:
        y = correction_map[y]

    return np.array((x, y))


def translate_position_to_button_number(position):
    """
    (-1,  1) 1  ( 0,  1) 2  ( 1,  1) 3
    (-1,  0) 4  ( 0,  0) 5  ( 1,  0) 6
    (-1, -1) 7  ( 0, -1) 8  ( 1, -1) 9
    """
    x, y = position[0], position[1]
    button_number = (x + 2) + (1 - y) * 3

    return button_number


if __name__ == '__main__':
    main()
