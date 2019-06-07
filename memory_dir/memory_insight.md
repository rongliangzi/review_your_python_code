# Python对象内存地址


[[Python对象内存地址]](https://blog.csdn.net/fragmentalice/article/details/81363494)
在python中，万物皆对象，常见的整数、浮点数、字符串、元祖、列表等类型，以及各种class、class instance等等都是对象。这些对象在python解释器内部的地址是怎样的呢？这里我们只简单看下python对象内存地址的相关基础知识，以及编码过程中一些注意事项，关于python解释器的内存管理机制，涉及到解释器内核的内存池原理，这里不做深入探讨，有兴趣的朋友可以去阅读解释器源代码。

0x01 不可变对象
    不可变对象是指对象的内存值不能被改变。Python中变量以引用的方式指向对象，如果变量引用了不可变对象，当改变该变量时，由于其所指的对象的值不能被改变，相当于把原来的值复制一份后再改变，这会开辟一个新的地址，变量再指向这个新的地址，即变量引用了新的对象。

    数值类型（整数和浮点）、字符串str、元组tuple都是不可变类型。比如a=1，b=[1]，c={'a':1}，id(a)、id(b[0])、id(1)、id(c['a'])将输出一样的值，因为1是不可变对象，其在内存中是不可改变的。

0x02 可变对象
    可变对象是指对象的内存值可以被改变，变量（准确的说是引用）改变后，实际上是其所指的值直接发生改变，并没有发生复制行为，也没有开辟新的内存地址，通俗点说就是原地改变。列表list、字典dict、集合set是可变类型。

0x03 对象的内存地址
    可以使用内置函数id()查看python对象的内存地址。下面是一些注意事项：

    (1) python中所有数字、字符串、list等值，创建时会分配内存空间，变量通过引用的方式使用它们。比如a=1和b=1，id(a)和id(b)的输出一样，表示a和b都指向相同的内存地址，即引用了同一个不可变对象；但是a=[1]和b=[1]，id(a)和id(b)将输出不一样的值，a和b指向的是不同的内存地址，即引用了不同的可变对象，说明各可变对象是相互独立的，在内存中有独立的内存地址；

    (2) 可用 is 判断两个对象的id（即内存地址）是否一样，用 == 判断两个对象的值是否一样。None值也有内存地址；

    (3) list、set对象有各自的独立内存空间，他们的各元素以引用的方式指向可变、不可变对象；

    (4) 函数形参的默认值，在内存中会开辟独立的内存空间。比如测试代码中test函数的param参数，其默认值是空list，如果调用时未传参，则param指向内存中预先分配好的地址，该地址存储的是list类型的值；当调用时传参为a，则param引用了a指向的内存空间；

    (5) python使用引用计数和垃圾回收来释放内存对象，每个内存对象都维护了一个引用计数，包括各种数字、字符串、list、set等类型值，以及类实例对象等等，当这些对象的引用计数为 0 时，会被解释器回收内存。每次对对象进行引用操作，都会导致其引用计数加1， 如下面测试代码中的整数1，列表a、b、c、d、n都引用了整数1，以及test函数中的append操作，都会导致数字1的引用计数加1；

    (6) copy和deepcopy方法都创建了新的内存对象，如测试代码中的b和c都是新的变量，其各个元素可能是指向同一个内存空间。赋值操作是指向同一个内存块，同时增加引用计数。copy是浅拷贝，deepcopy是深拷贝，特别对于可变对象，copy是以引用的方式指向同一个可变对象，而deepcopy会开辟新的内存地址，也就是创建了新的可变对象。