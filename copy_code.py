# encoding: utf-8
"""
@author:  Liangzi Rong
@contact: 289770334@qq.com
"""

import copy
import time


def copy_deepcopy():
    # copy is much more efficient
    a = range(10000)
    last_time = time.time()
    for i in range(10000):
        b = copy.copy(a)
    print('time(s) for copy: ', time.time() - last_time)
    last_time = time.time()
    for i in range(10000):
        b = copy.deepcopy(a)
    print('time(s) for deepcopy: ', time.time() - last_time)


if __name__ == '__main__':
    copy_deepcopy()
