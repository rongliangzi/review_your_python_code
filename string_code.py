# encoding: utf-8
"""
@author:  Liangzi Rong
@contact: 289770334@qq.com
"""
import time


def join_plus():
    str_list = ['']*int(1e8)
    last_time = time.time()
    str_a, str_b = '', ''
    for s in str_list:
        str_a += s
    print('time(s) for +=: ', time.time()-last_time)
    last_time = time.time()
    str_b = ''.join(str_list)
    print('time(s) for join: ', time.time()-last_time)


if __name__ == '__main__':
    join_plus()
