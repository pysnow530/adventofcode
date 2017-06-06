#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


def main():
    """入口"""
    s = open('day9.txt').read().strip()

    s_decompressed = decompress(s)
    print len(s_decompressed)


def decompress(s):
    """对s解压"""
    s_decompressed = ''

    while s:
        parse_result = try_parse_marker(s)

        if parse_result is not None:
            marker_length, repeat_length, repeat_times = parse_result

            s = s[marker_length:]
            s_decompressed += s[:repeat_length] * repeat_times
            s = s[repeat_length:]

        else:
            s_decompressed += s[0]
            s = s[1:]

    return s_decompressed


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
