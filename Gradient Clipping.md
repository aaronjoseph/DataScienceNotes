This is the process of clipping the gradients during backpropogation, so they never exceed a threshold

```py
optimizer = keras.optimize.SGD(clipvalue=1.0)
model.compile(loss="mse", optimizer = optimizer)
```