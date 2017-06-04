#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import numpy as np


RE_RECT = r'rect (\d+)x(\d+)'
RE_ROTATE = r'rotate (\w+) [xy]=(\d+) by (\d+)'


def main():
    """入口"""
    screen = Screen(50, 6)

    for cmd in open('day8.txt'):
        action, params = parse_cmd(cmd)

        if action == 'rect':
            a, b = params
            screen.rect(a, b)

        elif action == 'rrow':
            index, shifts = params
            screen.rotate_row(index, shifts)

        elif action == 'rcolumn':
            index, shifts = params
            screen.rotate_column(index, shifts)

    print screen.count_lit()


def parse_cmd(cmd):
    """解析指令，返回指令类型和参数
    rect 1x1                    =>  ('rect', (1, 1))
    rotate row y = 0 by 6       =>  ('rrow', (0, 6))
    rotate column y = 0 by 6    =>  ('rcolumn', (0, 6))
    """
    re_matched = re.match(RE_RECT, cmd)
    if re_matched:
        a, b = re_matched.groups()
        return ('rect', (int(a), int(b)))

    re_matched = re.match(RE_ROTATE, cmd)
    if re_matched:
        direction, index, shifts = re_matched.groups()
        return ('r' + direction, (int(index), int(shifts)))


class Screen(object):
    """模拟屏幕"""

    width = None
    height = None
    data = None

    def __init__(self, nr_column, nr_row):
        self.width = nr_column
        self.height = nr_row
        self.data = np.full((self.height, self.width), '.')

    def rect(self, a, b):
        self.data[:b,:a] = '#'

    def rotate_row(self, index, shifts):
        shifts = shifts % self.width

        self.data[index,:] = (list(self.data[index,-shifts:]) +
                              list(self.data[index,:-shifts]))

    def rotate_column(self, index, shifts):
        shifts = shifts % self.height

        self.data[:,index] = (list(self.data[-shifts:,index]) +
                              list(self.data[:-shifts,index]))

    def count_lit(self):
        """统计点亮个数"""
        return len(self.data[self.data == '#'])

    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    main()
