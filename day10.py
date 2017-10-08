#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
import re


def main():
    """入口"""
    bot_dict, output_dict = parse_from_file('day10.txt')

    while filter(Bot.has_two_chips, bot_dict.values()):
        for bot_no, bot in bot_dict.items():
            if bot.has_two_chips():
                # part1 答案
                if bot.chip_values == [17, 61]:
                    print bot_no

                bot.dispatch(bot_dict, output_dict)

    # part2 答案
    multiplier_list = []
    multiplier_list.extend(output_dict[0].chip_values)
    multiplier_list.extend(output_dict[1].chip_values)
    multiplier_list.extend(output_dict[2].chip_values)
    print reduce(int.__mul__, multiplier_list, 1)


def parse_from_file(fpath):
    """从文件中解析数据，返回 (bot字典, 转移字典) 元组"""
    re_goes = r'value (\d+) goes to bot (\d+)'
    re_give = (r'bot (\d+) gives low to (bot|output) (\d+) and '
               r'high to (bot|output) (\d+)')

    with open('day10.txt') as f:
        instructions = f.readlines()
        instructions = map(str.strip, instructions)

    bot_dict = collections.defaultdict(Bot)
    output_dict = collections.defaultdict(Output)

    # 初始化bot_dict
    for instruction in instructions:

        # 初始化芯片值
        give_matched = re.match(re_give, instruction)
        if give_matched:
            bot_no, low_type, low_receiver_no, high_type, high_receiver_no = \
                give_matched.groups()
            bot_no, low_receiver_no, high_receiver_no = \
                int(bot_no), int(low_receiver_no), int(high_receiver_no)

            bot = bot_dict[bot_no]
            bot.low_receiver_type = low_type
            bot.low_receiver_no = low_receiver_no
            bot.high_receiver_type = high_type
            bot.high_receiver_no = high_receiver_no

        # 初始化芯片转移信息
        goes_matched = re.match(re_goes, instruction)
        if goes_matched:
            value, bot_no = goes_matched.groups()
            value, bot_no = int(value), int(bot_no)

            bot_dict[bot_no].push_chip(value)

    return bot_dict, output_dict


class Bot(object):
    """Bot对象，包含芯片和转移信息"""

    chip_values = None

    low_receiver_type = None
    low_receiver_no = None

    high_receiver_type = None
    high_receiver_no = None

    def __init__(self):
        self.chip_values = []

    def push_chip(self, chip_value):
        """将某个值压入Bot，压入后，Bot将自动对比存放两个值"""
        self.chip_values.append(chip_value)
        self.chip_values.sort()

    def has_two_chips(self):
        """是否有两块芯片"""
        return len(self.chip_values) == 2

    def dispatch(self, bot_dict, output_dict):
        """转发两个值到其它 Bot 或 Output"""
        lower_value, higher_value = self.chip_values

        # 给出低值芯片
        if self.low_receiver_type == 'bot':
            low_receiver = bot_dict[self.low_receiver_no]
        elif self.low_receiver_type == 'output':
            low_receiver = output_dict[self.low_receiver_no]
        low_receiver.push_chip(lower_value)

        # 给出高值芯片
        if self.high_receiver_type == 'bot':
            high_receiver = bot_dict[self.high_receiver_no]
        elif self.high_receiver_type == 'output':
            high_receiver = output_dict[self.high_receiver_no]
        high_receiver.push_chip(higher_value)

        # 清空自己的芯片
        self.chip_values = []


class Output(object):
    """输出对象，可接收芯片"""

    chip_values = None

    def __init__(self):
        self.chip_values = []

    def push_chip(self, chip_value):
        """将某个值压入Bot，压入后，Bot将自动对比存放两个值"""
        self.chip_values.append(chip_value)


if __name__ == '__main__':
    main()
