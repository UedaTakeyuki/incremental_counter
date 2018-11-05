# incremental-counter
Incremental Counter

```python:
>>> import counter
>>> c = counter.Counter("/tmp/counter.txt")
>>> c.current()
0
>>> c.inc()
1
>>> c.inc()
2
>>> c.reset()
0
>>> c.set(3)
3
>>> c.dec()
2
>>> c.dec()
1
>>> c.dec()
0
>>> c.dec()
0
>>> c.dec()
0
```
