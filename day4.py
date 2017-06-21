#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import string
import collections


def main():
    """入口"""
    real_rooms = []

    with open('day4.txt') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        name, sector_id, checksum = parse_info(line)

        if is_real_room(name, checksum):
            real_rooms.append({
                'sector_id': sector_id,
                'name': name,
                'decrypted_name': decrypt_name(name, sector_id),
                'checksum': checksum,
            })

    print sum([r['sector_id'] for r in real_rooms])
    print [i for i in real_rooms if 'northpole' in i['decrypted_name']]


def parse_info(line):
    """分析一行数据，获取name、sector_id、checksum"""
    re_match = re.match(r'^([a-z-]+)(\d+)\[(\w+)\]$', line)
    name, sector_id, checksum = re_match.groups()
    sector_id = int(sector_id)

    return name, sector_id, checksum


def is_real_room(name, checksum):
    """判断是否是一个真实的房间
    将checksum的字符去除，取其中最小的出现次数，看剩下的字符是否有
    大于该次数的字符
    """
    counter = collections.Counter(name)

    counter.pop('-')

    # 取checksum的最小出现次数
    checksum_min_times = min(map(counter.__getitem__, checksum))

    # 将checksum的字符从counter中去掉
    map(counter.pop, filter(counter.has_key, checksum))

    # 取剩下字符的最大出现次数
    most_common = counter.most_common(1)
    left_max_times = most_common[0][1] if most_common else -1

    return left_max_times <= checksum_min_times


def decrypt_name(name, sector_id):
    """使用sector_id对name解密"""
    name = name.replace('-', ' ')

    # 创建转换表
    alphabet = string.ascii_lowercase
    nr_shift = sector_id % len(alphabet)
    trans = string.maketrans(alphabet, alphabet[nr_shift:]+alphabet[:nr_shift])

    decrypted_name = string.translate(name, trans)

    return decrypted_name


if __name__ == '__main__':
    main()
