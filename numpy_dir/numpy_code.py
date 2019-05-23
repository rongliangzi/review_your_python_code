# encoding: utf-8
"""
@author:  Liangzi Rong
@contact: 289770334@qq.com
"""
import time
import numpy as np


# 顺序读取效率
def get_np_list(size=(200, 100), iteration=100):
    np_matrix = np.zeros(size)
    list_matrix = [[0] * size[1]] * size[0]
    last_time = time.time()
    for i in range(iteration):
        for j in range(size[0]):
            for k in range(size[1]):
                a = np_matrix[j][k]
    print('time(s) for np_matrix: ', time.time()-last_time)
    last_time = time.time()
    for i in range(iteration):
        for j in range(size[0]):
            for k in range(size[1]):
                a = list_matrix[j][k]
    print('time(s) for list_matrix: ', time.time()-last_time)


# built-in flip and reverse
def flip():
    raw = np.eye(4)
    raw_flip_lr = np.fliplr(raw)
    raw_reversed_lr = raw[:, ::-1, ...]
    raw_flip_ud = np.flipud(raw)
    raw_reversed_ud = raw[::-1, ...]


if __name__ == '__main__':
    get_np_list()
