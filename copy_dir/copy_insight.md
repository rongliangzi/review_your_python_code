# Insight about copy in python

## :monkey: '=' & copy.copy() & copy.deepcopy()
- '=' just give the id(raw) to copy_0, meaning raw and copy_0 point at the same memory block
- copy.copy() is shallow copy, which just store the contents of raw not containing sub-variable. For the contents
containing sub-variables, it choose to point at the same memory block just as '=' does, such as raw[1]=[2, 3]
- copy.deepcopy() is deep copy, which create a memory block to store the whole contents of raw 
:monkey: we can call func `id()` to check the memory address

```
copy_0 = raw
copy_1 = copy.copy(raw)
copy_2 = copy.deepcopy(raw)
```