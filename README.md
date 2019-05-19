# Review your python code
Let's write python code efficiently and elegantly

编写高效，优雅的python代码!

Python is one of the most popular programming languages, and it's easy to understand. It's assumed that you're able to 
write python code, but the problem lies in how to write it well, namely efficiently, elegantly, easy to read for others 
and name the variable properly.

Python是最受欢迎的编程语言之一，易上手，好理解。很多人可以编写一些能够运行Python代码，但是我们希望代码能运行的更加高效，写的更加规范，
易读，这也是本repo的目的所在。
## Contents

- :syringe: [numpy](https://github.com/rongliangzi/review_your_python_code/tree/master/numpy_dir/numpy_insight.md)
- :droplet: [string](https://github.com/rongliangzi/review_your_python_code/tree/master/string_dir/string_insight.md)
- :cow: [list](https://github.com/rongliangzi/review_your_python_code/tree/master/list_dir/list_insight.md)
- :beer: [copy](https://github.com/rongliangzi/review_your_python_code/tree/master/copy_dir/copy_insight.md)
- :tongue: [built-in funcs](https://github.com/rongliangzi/review_your_python_code/tree/master/built_in_func_dir/built_in_func_insight.md)
- :dog: to be continued

## Examples
For example, original code is:
```
for s in str_list:
    str_a += s
```
`.join()` is more efficient than `+=` for string connection, so it's better to write like:
```
str_a = ''.join(a)
```
The actual running time(len(a)=1e8) is:
```
time for +=:  2.5960795879364014s
time for join:  0.357041597366333s
```
Another example:
```
Class appletree():
    def leaf():
        pass
```
We usually use `Camel-Case` in class name, that is, it's better to define the class like this:
```
Class AppleTree():
    def leaf():
        pass
```