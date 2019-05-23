# encoding: utf-8
"""
@author:  Liangzi Rong
@contact: 289770334@qq.com
"""
import time


def timer(func, iteration):
    start = time.time()
    func(iteration)
    print(time.time()-start)
