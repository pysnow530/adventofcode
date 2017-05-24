#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import itertools


door_id = 'cxdnnyjw'
password_length = 8


password = ''

for i in itertools.count(0):
    hexdigest = hashlib.md5(door_id + str(i)).hexdigest()

    if hexdigest.startswith('00000'):
        password += hexdigest[5]

        if len(password) >= password_length:
            print password
            break
