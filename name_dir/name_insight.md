# Insights of name

Name dynamically
```
# use setattr() to 
class Name():
    # self.var0=0 ... self.vark=k
    def __init__(self, count):
        for i in range(count):
            setattr(self, 'var'+str(i), i)
```