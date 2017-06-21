#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys


def main():
    """入口"""
    with open('day10.txt') as f:
        direction_list = f.readlines()
        direction_list = map(str.strip, direction_list)

    # 初始化bot {0: [5], 1: [1, 2], 2: [3], 3: []}
    bot_dict = {}
    for direction in direction_list:
        goes_tuple = parse_goes(direction)
        if goes_tuple is None:
            continue

        value, bot = goes_tuple
        if bot not in bot_dict:
            bot_dict[bot] = []
        bot_dict[bot].append(value)

    # 初始化转移字典
    give_dict = {}
    for direction in direction_list:
        give_info = parse_give(direction)
        if give_info is None:
            continue

        bot = give_info['bot']
        give_dict[bot] = give_info

    output_dict = {}
    while True:
        # 查找同时具有low和high值的bot
        try:
            two_microchips_bot = [bot for bot, value_list in bot_dict.items()
                                  if len(value_list) == 2][0]
        except Exception:       # 已不存在同时具有low和hight值的bot
            print output_dict[0][0] * output_dict[1][0] * output_dict[2][0]
            sys.exit()

        value_list = bot_dict[two_microchips_bot]
        low_value, high_value = min(value_list), max(value_list)

        # part 1求解
        if low_value == 17 and high_value == 61:
            print two_microchips_bot

        # 执行转移
        low_to = give_dict[two_microchips_bot]['low_to']['number']
        if give_dict[two_microchips_bot]['low_to']['type'] == 'bot':
            if low_to not in bot_dict:
                bot_dict[low_to] = []
            bot_dict[low_to].append(low_value)
        elif give_dict[two_microchips_bot]['low_to']['type'] == 'output':
            if low_to not in output_dict:
                output_dict[low_to] = []
            output_dict[low_to].append(low_value)

        high_to = give_dict[two_microchips_bot]['high_to']['number']
        if give_dict[two_microchips_bot]['high_to']['type'] == 'bot':
            if high_to not in bot_dict:
                bot_dict[high_to] = []
            bot_dict[high_to].append(high_value)
        elif give_dict[two_microchips_bot]['high_to']['type'] == 'output':
            if high_to not in output_dict:
                output_dict[high_to] = []
            output_dict[high_to].append(high_value)

        bot_dict[two_microchips_bot] = []


def parse_goes(direction):
    """解析赋值指令，返回描述指令的元组
    value 5 goes to bot 2   =>  (5, 2)
    """
    re_goes = r'value (\d+) goes to bot (\d+)'

    re_matched = re.match(re_goes, direction)
    if re_matched:
        value, bot = re_matched.groups()
        value, bot = int(value), int(bot)
        return (value, bot)
    else:
        return None


def parse_give(direction):
    """解析分发指令，返回描述指令的元组（过滤输出到output的值）
    bot 1 gives low to output 1 and high to bot 0 => (1, 0)
    """
    re_give = (r'bot (\d+) gives low to (bot|output) (\d+) and '
               r'high to (bot|output) (\d+)')

    re_matched = re.match(re_give, direction)

    if re_matched:
        bot, low_type, low_bot, high_type, high_bot = re_matched.groups()
        bot, low_bot, high_bot = int(bot), int(low_bot), int(high_bot)

        return {
            'bot': bot,
            'low_to': {
                'type': low_type,
                'number': low_bot,
            },
            'high_to': {
                'type': high_type,
                'number': high_bot,
            }
        }

    else:
        return None


if __name__ == '__main__':
    main()
