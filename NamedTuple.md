- Namedtuple is like a light-weight object
	- Like tuple, but is more readable

```python

#Assume you are storing the values of colour
color = (55,155,255) # Assume, you are storing the RGB values

Color = NamedTuple('Color',['red','green','blue'])

White = Color(255,255,255)

```