#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


RE_MARKER = re.compile(r'^(\((\d+)x(\d+)\))')


def main():
    """入口"""
    s = open('day9.txt').read().strip()

    print count_depressed_length(s)
    print count_depressed_length2(s)


def count_depressed_length(s):
    """统计解密后的文本长度"""
    if s == '':
        return 0

    parse_result = try_parse_marker(s)

    if parse_result is not None:
        marker_length, repeat_length, repeat_times = parse_result
        return (repeat_length * repeat_times +
                count_depressed_length(s[marker_length+repeat_length:]))

    else:
        return 1 + count_depressed_length(s[1:])


def count_depressed_length2(s):
    """统计解密后的文本长度（支持递归展开）"""
    count = 0

    while s != '':
        parse_result = try_parse_marker(s)

        if parse_result is not None:
            marker_length, repeat_length, repeat_times = parse_result

            repeat_text = s[marker_length:marker_length+repeat_length]
            count += count_depressed_length2(repeat_text) * repeat_times

            s = s[marker_length+repeat_length:]

        else:
            count += 1
            s = s[1:]

    return count


def try_parse_marker(s):
    """尝试解析s头的marker，如果不是marker，返回None，否则返回
    (marker_length, repeat_length, repeat_times)
    """
    re_matched = RE_MARKER.match(s)

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
