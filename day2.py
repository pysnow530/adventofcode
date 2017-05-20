#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

import numpy as np


BUTTON_NUMBER_MAP1 = {
    '(-1, 1)' : 1, '(0, 1)' : 2, '(1, 1)' : 3,
    '(-1, 0)' : 4, '(0, 0)' : 5, '(1, 0)' : 6,
    '(-1, -1)': 7, '(0, -1)': 8, '(1, -1)': 9,
}

BUTTON_NUMBER_MAP2 = {
                                   '(0, 2)' :  1 ,
                  '(-1, 1)' :  2 , '(0, 1)' :  3 , '(1, 1)' :  4 ,
    '(-2, 0)': 5, '(-1, 0)' :  6 , '(0, 0)' :  7 , '(1, 0)' :  8 , '(2, 0)': 9,
                  '(-1, -1)': 'A', '(0, -1)': 'B', '(1, -1)': 'C',
                                   '(0, -2)': 'D',
}

BUTTON_NUMBER_MAP = BUTTON_NUMBER_MAP2


def main():
    """入口"""
    current_position = np.array((0, 0))

    instructions = open('day2.txt').readlines()

    for instruction in instructions:
        instruction = instruction.strip()

        for direction_char in instruction:
            direction = translate_char_to_direction(direction_char)
            current_position += direction
            current_position = correct_position(current_position, direction)

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


def correct_position(position, last_direction):
    """如果超出范围，修正位置"""
    x, y = position
    position_str = '(%d, %d)' % (x, y)

    if BUTTON_NUMBER_MAP.get(position_str) is None:
        return position - last_direction
    else:
        return position


def translate_position_to_button_number(position):
    """
    (-1,  1) 1  ( 0,  1) 2  ( 1,  1) 3
    (-1,  0) 4  ( 0,  0) 5  ( 1,  0) 6
    (-1, -1) 7  ( 0, -1) 8  ( 1, -1) 9
    """
    x, y = position[0], position[1]
    position_str = '(%d, %d)' % (x, y)
    button_number = BUTTON_NUMBER_MAP.get(position_str)

    return button_number


if __name__ == '__main__':
    main()
