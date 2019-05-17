# Review your python code
Let's write python code efficiently and elegantly

Python is one of the most popular programming languages, and it's easy to understand. It's assumed that you're able to 
write python code, but the problem lies in how to write it well, namely efficiently, elegantly, easy to read for others 
and name the variable properly.

For example, original code is:
```
for s in str_list:
    str_a += s
```
.join() is more efficient than += for string connection, so it's better to write like:
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
We usually use Camel-Case in class name, that is, it's better to define the class like this:
```
Class AppleTree():
    def leaf():
        pass
```