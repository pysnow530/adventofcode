#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import collections


def main():
    """入口"""
    sector_id_sum = 0

    for line in open('day4.txt'):
        line = line.strip()
        line = line.replace('-', '')

        re_match = re.match(r'^([a-z]+)(\d+)\[(\w+)\]$', line)
        name, sector_id, checksum = re_match.groups()

        if is_real_room(name, checksum):
            sector_id_sum += int(sector_id)

    print sector_id_sum


def is_real_room(name, checksum):
    """判断是否是一个真实的房间
    将checksum的字符去除，取其中最小的出现次数，看剩下的字符是否有
    大于该次数的字符
    """
    counter = collections.Counter(name)

    # 取checksum的最小出现次数
    checksum_min_times = min(map(counter.__getitem__, checksum))

    # 将checksum的字符从counter中去掉
    map(counter.pop, filter(counter.has_key, checksum))

    # 取剩下字符的最大出现次数
    most_common = counter.most_common(1)
    left_max_times = most_common[0][1] if most_common else -1

    return left_max_times <= checksum_min_times


if __name__ == '__main__':
    main()
