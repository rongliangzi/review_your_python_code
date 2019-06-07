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
        _ = copy.copy(a)
    print('time(s) for copy: ', time.time() - last_time)
    last_time = time.time()
    for i in range(10000):
        _ = copy.deepcopy(a)
    print('time(s) for deepcopy: ', time.time() - last_time)


def dif_copy_func():
    a = 1
    b = a
    a = 2
    print('b value after a value is changed to 2: ', b)
    print('id(a): ', id(a), ',id(b): ', id(b))

    raw = [1, [2, 3]]
    # = just give the id(raw) to copy_0, meaning raw and copy_0 point at the same memory block
    copy_0 = raw
    # copy.copy() is shallow copy, which just store the contents of raw not containing sub-variable. For the contents
    # containing sub-variables, it choose to point at the same memory block just as '=' does, such as raw[1]=[2, 3]
    copy_1 = copy.copy(raw)
    # copy.deepcopy() is deep copy, which create a memory block to store the whole contents of raw
    copy_2 = copy.deepcopy(raw)
    print('id(raw):{0}, id(copy_0):{1}, id(copy_1):{2}, id(copy_2):{3}'.format(id(raw), id(copy_0), id(copy_1), id(copy_2)))
    print('id(raw[1]):{0}, id(copy_1[1]):{1}'.format(id(raw[1]), id(copy_1[1])))
    raw[0] = 0
    print('raw:{0}, copy_0:{1} ,copy_1:{2}, copy_2:{3}'.format(raw, copy_0, copy_1, copy_2))
    raw[1].append(5)  # but if write like: raw[2]=[3, 4, 5], copy_1[2] will be [3, 4] not [3, 4, 5]
    print('raw:{0}, copy_0:{1} ,copy_1:{2}, copy_2:{3}'.format(raw, copy_0, copy_1, copy_2))
    raw.append(100)
    print('raw:{0}, copy_0:{1} ,copy_1:{2}, copy_2:{3}'.format(raw, copy_0, copy_1, copy_2))


if __name__ == '__main__':
    # copy_deepcopy()
    dif_copy_func()
