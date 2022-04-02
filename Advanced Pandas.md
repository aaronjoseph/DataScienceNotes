#oan 

**To send one column into a function and get the output** 
```python
zip(*df[columns].map(function_name))
```

**To send multiple column into a function** 
```python
df.apply(lambda x: function(x.col_1, x.col_2), axis=1)
df[['col_1','col_2']].apply(lambda x: f(*x), axis=1)
```



