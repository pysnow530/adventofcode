#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


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
        give_tuple = parse_give(direction)
        if give_tuple is None:
            continue

        bot, low_to_bot, high_to_bot = give_tuple
        give_dict[bot] = {'low_to_bot': low_to_bot, 'high_to_bot': high_to_bot}

    while True:
        # 查找同时具有low和high值的bot
        two_microchips_bot = [bot for bot, value_list in bot_dict.items()
                              if len(value_list) == 2][0]

        value_list = bot_dict[two_microchips_bot]
        low_value, high_value = min(value_list), max(value_list)

        # part 1求解
        if low_value == 17 and high_value == 61:
            print two_microchips_bot
            break

        low_to_bot = give_dict[two_microchips_bot]['low_to_bot']
        high_to_bot = give_dict[two_microchips_bot]['high_to_bot']

        # 执行转移
        if low_to_bot is not None:
            if low_to_bot not in bot_dict:
                bot_dict[low_to_bot] = []
            bot_dict[low_to_bot].append(low_value)
        if high_to_bot is not None:
            if high_to_bot not in bot_dict:
                bot_dict[high_to_bot] = []
            bot_dict[high_to_bot].append(high_value)

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

        if low_type == 'bot' and high_type == 'bot':
            return (bot, low_bot, high_bot)
        elif low_bot == 'bot' and high_type == 'output':
            return (bot, low_bot, None)
        elif low_type == 'output' and high_type == 'bot':
            return (bot, None, high_bot)
        elif low_type == 'output' and high_type == 'output':
            return (bot, None, None)

    else:
        return None


if __name__ == '__main__':
    main()
