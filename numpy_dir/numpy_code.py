# encoding: utf-8
"""
@author:  Liangzi Rong
@contact: 289770334@qq.com
"""
import time
import numpy as np
import sys


# 顺序读取效率
def get_np_list(size=(200, 100), iteration=100):
    np_matrix = np.arange(0, size[0]*size[1]).reshape(size)
    list_matrix = [[i*size[1]+j for j in range(size[1])] for i in range((size[0]))]
    print('id(np_matrix[0]): {0}, id(np_matrix[1]): {1}'.format(id(np_matrix[0]), id(np_matrix[1])))
    print('id(list_matrix[0]): {0}, id(list_matrix[1]): {1}, data length: {2}'.
          format(id(list_matrix[0]), id(list_matrix[1]), sys.getsizeof(list_matrix[0])))
    last_time = time.time()
    for i in range(iteration):
        for j in range(size[0]):
            for k in range(size[1]):
                _ = np_matrix[j][k]
    print('\ntime(s) for iterating np_matrix: ', time.time()-last_time)
    last_time = time.time()
    for i in range(iteration):
        for j in range(size[0]):
            for k in range(size[1]):
                _ = list_matrix[j][k]
    print('\ntime(s) for iterating list_matrix: ', time.time()-last_time)
    last_time = time.time()
    for _ in range(iteration):
        _ = np_matrix.sum()
    print(np_matrix.sum())
    print('\ntime(s) for list_matrix sum: ', time.time() - last_time)
    last_time = time.time()
    s = 0
    for _ in range(iteration):
        s = 0
        for i in range(size[0]):
            for j in range(size[1]):
                s += list_matrix[i][j]
    print(s)
    print('\ntime(s) for list_matrix sum: ', time.time() - last_time)
    last_time = time.time()


# built-in flip and reverse
def flip():
    raw = np.arange(0, 12).reshape((2, 2, 3))
    print(raw)
    raw_flip_lr = np.fliplr(raw)
    raw_reversed_lr = raw[:, ::-1, ...]
    raw_flip_ud = np.flipud(raw)
    raw_reversed_ud = raw[::-1, ...]
    print('\n', raw_flip_lr)
    print('\n', raw_reversed_lr)
    print('\n', raw_flip_ud)
    print('\n', raw_reversed_ud)


# copy array/复制向量，如将一个(2,3)的扩展为(3,2,3)的，可以(2,3)->(1,2,3)->(3,2,3)
def repeat():
    # np.repeat：复制的是多维数组的每一个元素,返回一个flatten的array；
    # axis来控制复制的行和列，可以复制多维数组本身，返回高维数组，而非flatten的一维数组
    # axis参数指定某一维时，可以实现该维度中不同子数组不同的复制次数
    # np.tile：复制的是多维数组本身；
    raw = np.linspace(1, 6, 6)
    raw = raw.reshape([1, 2, 3])
    print('raw shape: ', raw.shape, '\nraw array: ', raw)
    raw_rp = np.repeat(raw, 2)
    print('\n2 repeats every element and flatten array shape(1D): ', raw_rp.shape, '\ncontent: ', raw_rp)
    raw_rp = np.repeat(raw, 2, axis=0)
    print('\n2 repeats specify axis(dimensions not changed) shape:', raw_rp.shape, '\ncontent ', raw_rp)
    raw_rp = np.repeat(raw, (1, 2), axis=1)
    print('\n2 repeats dif repetitions in specific axis(dimensions not changed): ', raw_rp.shape, '\ncontent: ', raw_rp)
    raw_tile = np.tile(raw, (2, 1, 1))
    print('\n2 repeats tile(dimensions not changed) shape: ', raw_tile.shape, '\ncontent: ', raw_tile)


if __name__ == '__main__':
    get_np_list()
    # flip()
    # repeat()
