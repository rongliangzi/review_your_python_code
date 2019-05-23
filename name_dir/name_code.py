# encoding: utf-8
"""
@author:  Liangzi Rong
@contact: 289770334@qq.com
"""


class Name():
    def __init__(self, count):
        for i in range(count):
            setattr(self, 'var'+str(i), i)
