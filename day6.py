#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
import collections

import pandas as pd


def main():
    """入口"""
    with open('day6.txt') as f:
        lines = f.readlines()
        lines = map(string.strip, lines)

    # 获取字符矩阵
    char_matrix = map(list, lines)

    # 转置
    data_frame = pd.DataFrame(char_matrix)
    char_matrix_t = data_frame.T.values

    # 连接最大出现次数的字符
    print ''.join([collections.Counter(i).most_common()[0][0]
                  for i in char_matrix_t])

    # 连接最小出现次数的字符
    print ''.join([collections.Counter(i).most_common()[-1][0]
                  for i in char_matrix_t])


if __name__ == '__main__':
    main()
