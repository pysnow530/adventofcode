#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    """入口"""
    with open('day7.txt') as f:
        ipv7_list = f.readlines()

    tls_supported_ipv7_list = filter(tls_supported, ipv7_list)
    print len(tls_supported_ipv7_list)

    ssl_supported_ipv7_list = filter(ssl_supported, ipv7_list)
    print len(ssl_supported_ipv7_list)


def tls_supported(ipv7):
    """判断一个ipv7是否支持tls"""
    no_bracket_segments, bracket_segments = parse_ipv7(ipv7)

    if (any(map(match_abba, no_bracket_segments)) and
            (not any(map(match_abba, bracket_segments)))):
        return True
    else:
        return False


def ssl_supported(ipv7):
    """判断一个ipv7是否支持ssl"""
    no_bracket_segments, bracket_segments = parse_ipv7(ipv7)

    no_bracket_aba_list = reduce(list.__add__,
                                 map(parse_aba_list, no_bracket_segments),
                                 [])
    bracket_aba_list = reduce(list.__add__,
                              map(parse_aba_list, bracket_segments),
                              [])

    for no_bracket_aba in no_bracket_aba_list:
        if corresponding_aba(no_bracket_aba) in bracket_aba_list:
            return True
    else:
        return False


def parse_ipv7(ipv7):
    """解析ipv7，返回[]外和[]内的两个数组"""
    no_bracket_segments = []
    bracket_segments = []

    segments = ipv7.split('[')
    for segment in segments:
        if ']' in segment:
            bracket_segment, no_bracket_segment = segment.split(']')
            bracket_segments.append(bracket_segment)
            no_bracket_segments.append(no_bracket_segment)
        else:
            no_bracket_segments.append(segment)

    return no_bracket_segments, bracket_segments


def match_abba(s):
    """是否包含ABBA模式的字符串"""
    for i in range(0, len(s) - 3):
        ch0, ch1, ch2, ch3 = s[i:i+4]
        if ch0 == ch3 and ch1 == ch2 and ch0 != ch1:
            return True

    return False


def parse_aba_list(s):
    """解析字符串，返回aba模式的列表"""
    aba_list = []

    for i in range(0, len(s)-2):
        ch0, ch1, ch2 = s[i:i+3]
        if ch0 == ch2 and ch0 != ch1:
            aba_list.append(s[i:i+3])

    return list(set(aba_list))


def corresponding_aba(aba):
    """将aba转换为bab的模式"""
    a, b, _ = aba

    return b + a + b


if __name__ == '__main__':
    main()
