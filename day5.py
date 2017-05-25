#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import itertools


def main():
    """入口"""
    door_id = 'cxdnnyjw'
    password_length = 8


    valid_hashes = []

    for i in itertools.count(0):
        if password2_cracked(valid_hashes):
            break

        hexdigest = hashlib.md5(door_id + str(i)).hexdigest()

        if hexdigest.startswith('00000'):
            valid_hashes.append(hexdigest)

    print calculate_password1(valid_hashes), calculate_password2(valid_hashes)


def password2_cracked(valid_hashes):
    """判断password2是否已破解"""
    positions = [h[5] for h in valid_hashes]
    position_filled_list = map(positions.__contains__, '01234567')

    return all(position_filled_list)


def calculate_password1(valid_hashes):
    """计算password1"""
    return ''.join([i[5] for i in valid_hashes[:8]])


def calculate_password2(valid_hashes):
    """计算password2"""
    password_chars = [None] * 8

    for valid_hash in valid_hashes:
        position, password_char = valid_hash[5:7]

        if position.isdigit():
            position = int(position)
            if position < 8 and password_chars[position] is None:
                password_chars[position] = password_char

        if None not in password_chars:
            return ''.join(password_chars)


if __name__ == '__main__':
    main()
