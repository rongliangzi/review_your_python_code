# Insights of numpy

我们都爱`numpy`！！！

[[为什么NumPy数组如此高效？]](https://www.cnblogs.com/McKean/p/6221053.html)

一个NumPy数组基本上是由元数据（维数、形状、数据类型等）和实际数据构成。**数据存储在一个均匀连续的内存块中**，该内存在系统内存（随机
存取存储器，或RAM）的一个特定地址处，被称为数据缓冲区。这是和list等纯Python结构的主要区别，**list的元素在系统内存中是分散存储的。**
这是使NumPy数组如此高效的决定性因素。

[[数组的创建与存储]](https://www.cnblogs.com/moon1992/p/4946717.html)
### `list`和`ndarray`的效率
`list`和`ndarray`都可以存储矩阵，但`ndarray`每维度长度一样，`list`则不必。如`[[1],[2,3]]`。那么读取效率谁更高呢？答案是`list`，在100次
顺序读取`(200,100)`大小的矩阵时间测试中，两者效率如下，`list`明显高于`ndarray`，那为什么还要使用`ndarray`呢，因为在`ndarray`中使用循环
是非常低效的，应该尽量使用矩阵操作或内置函数，例如代码中的100次`sum`用时为`ndarray:list=0.00295:0.12868`。奇怪的是，使用`id`函数取
`ndarray`中任意元素或子向量的地址都是同一个地址，即`id(np_matrix[0])==id(np_matrix[1]) is always True`，猜想可能是存储了`ndarray`的起始位置，
访问元素时使用起始位置+偏置

```
id(np_matrix[0]): 2436284015920, id(np_matrix[1]): 2436284015920
id(list_matrix[0]): 2436284160520, id(list_matrix[1]): 2436284166600, data length: 912
time(s) for iterating np_matrix:  0.4358022212982178
time(s) for iterating list_matrix:  0.08477139472961426

time(s) for list_matrix sum:  0.0009965896606445312
time(s) for list_matrix sum:  0.1266632080078125
```
### copy array/复制向量
如将一个(2,3)的向量扩展为(3,2,3)的，可以(2,3)reshape->(1,2,3)(tile/repeat)->(3,2,3)

### flip/翻转矩阵(上下/左右)
输入向量至少2D，上下翻转flipud()，针对第0维，等价于`raw_reversed_ud = raw[::-1, ...]`,左右反转针对第1维，等价于`raw_reversed_ud = raw[:,::-1, ...]`


