#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:yuzai
@file:main.py
@time:2022/09/17

"""
from Qndxx import Qndxx
import os

if __name__ == '__main__':
    # 这里需要在github中设置
    laravel_session = os.environ["COOKIE1"]
    qndxx = Qndxx(laravel_session)
    qndxx.login()
    qndxx.confirm()
