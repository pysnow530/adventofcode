#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def main():
    """入口"""
    s = open('day9.txt').read().strip()

    print count_depressed_length(s)


def count_depressed_length(s):
    """统计解密后的文本长度"""
    if s == '':
        return 0

    parse_result = try_parse_marker(s)

    if parse_result is not None:
        marker_length, repeat_length, repeat_times = parse_result
        return (repeat_length*repeat_times +
                count_depressed_length(s[marker_length+repeat_length:]))

    else:
        return 1 + count_depressed_length(s[1:])


def try_parse_marker(s):
    """尝试解析s头的marker，如果不是marker，返回None，否则返回
    (marker_length, repeat_length, repeat_times)
    """
    re_matched = re.match(r'^(\((\d+)x(\d+)\))', s)

    if re_matched:
        marker, repeat_length, repeat_times = re_matched.groups()

        marker_length = len(marker)
        repeat_length = int(repeat_length)
        repeat_times = int(repeat_times)

        return (marker_length, repeat_length, repeat_times)

    else:
        return None


if __name__ == '__main__':
    main()
