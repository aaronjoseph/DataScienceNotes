There are times when you need to apply certain customer functions on a pandas dataframe, this can be done with apply

---

Assume, you want to make the any value under 2 as NaN for a certain column in pandas

```py 
def filter_v(values):
	if value <2:
		return np.nan
	else:
		return value
		
data['cleaned_b'] = data['b'].apply(filter_v)
```


