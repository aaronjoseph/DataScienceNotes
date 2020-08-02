This is the process of grouping continious values into smaller discrete groups

```py
pd.cut(DF['Target'],
bins = [0.,1.5,3.0,4.5,6.,np.inf],
labels = [1,2,3,4,5])
```
