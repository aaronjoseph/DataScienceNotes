### Sequential Models

To develop sequential model in Keras

```py
from tensorflow import keras

# Code to create a rudimentary model
model = keras.models.Sequential([
keras.layers.Flatten(),
keras.layers.Dense(300,activation='relu'),
keras.layers.Dense(100,activation='relu'),
keras.layers.Dense(10,activation='softmax')
])

model.summary()

# Code to check the layers weight and bias
hidden1 = model.layers[1]
hidden1.name # Gives the layer name -> Dense
hidden1.get_weights() # Gives the Weight and Bias

model.complie(loss="sparse_categorical_crossentropy",
optimizer="sgd",
metrics=["accuracy"])

# Code to Fit
history = model.fit(X_Train,Y_Train, epochs=30, 
# Validation Data
validation_data = (X_Valid,Y_Valid))

# To see performance
history.history # Has the metrics

# Evaluation
model.evaluate(X_Test,Y_Test)

# Model Prediction
model.predict(X_Pred)
```

[[Entropy, Cross-Entropy, Sparse_Cross_Entropy and KL Divergence]] For Sparse_Categorical Entropy

---
Designing model with specific structure
```py
input_A = keras.layers.Input(shape=[5], name="wide_input")
input_B = keras.layers.Input(shape=[6], name="deep_input")
hidden1 = keras.layers.Dense(30,activation="relu")(input_B)
hidden2 = keras.layers.Dense(30,activation="relu")(hidden1)
concat = keras.layers.concatenate([input_A, hidden2])
output = keras.layers.Dense(1, name="output")(concat)
# Final Design Consolidation
model = keras.models.Model(inputs=[input_A,input_B], outputs=[output])
model.compile(loss="mse",optimizer=keras.optimizer.SGD(lr=1e-3))
```

--- 
Using Subclassing API

```py
class WideAndDeepModel(keras.models.Model):
    def __init__(self, units=30, activation="relu", **kwargs):
        super().__init__(**kwargs)
        self.hidden1 = keras.layers.Dense(units, activation=activation)
        self.hidden2 = keras.layers.Dense(units, activation=activation)
        self.main_output = keras.layers.Dense(1)
        self.aux_output = keras.layers.Dense(1)
        
    def call(self, inputs):
        input_A, input_B = inputs
        hidden1 = self.hidden1(input_B)
        hidden2 = self.hidden2(hidden1)
        concat = keras.layers.concatenate([input_A, hidden2])
        main_output = self.main_output(concat)
        aux_output = self.aux_output(hidden2)
        return main_output, aux_output

model = WideAndDeepModel(30, activation="relu")
```

--- 
Saving & Loading the model & Weights

Keras models can be saved in HDF5 format

```py
# Saving Model
model.save('model.h5')
#Loading the model
keras.model.load_model('model.h5')
# Saving Weights
model.save_weights("weights.ckpt")
# Loading Weights
model.load_weights("weights.ckpt")
```

--- 
Callbacks

keras.callbacks.ModelCheckpoint() saves checkpoints of the model at regular intervals during training -> at end of each epoch

```py
checkpoint_cb = keras.callbacks.ModelCheckpoint("model.h5",
save_best_only=True # This to be used when using validation set
)
model.fit(.....,callbacks=[checkpoint_cb])
```

### Earlystopping
This can be done as follows

```py
early_stopping_cb = keras.callbacks.EarlyStopping(patience=10,restore_best_weights=True)
model.fit(....,callbacks=[checkpoint_cb,early_stopping_cb])
```

---

### Tensorboard

```py
# Code approach
def get_run_logdir():
    import time
    run_id = time.strftime("run_%Y_%m_%d-%H_%M_%S")
    return os.path.join(root_logdir, run_id)

run_logdir = get_run_logdir()
run_logdir

keras.backend.clear_session()
np.random.seed(42)
tf.random.set_seed(42)

model = keras.models.Sequential([
    keras.layers.Dense(30, activation="relu", input_shape=[8]),
    keras.layers.Dense(30, activation="relu"),
    keras.layers.Dense(1)
])    
model.compile(loss="mse", optimizer=keras.optimizers.SGD(lr=1e-3))

tensorboard_cb = keras.callbacks.TensorBoard(run_logdir)
history = model.fit(X_train, y_train, epochs=30,
                    validation_data=(X_valid, y_valid),
                    callbacks=[checkpoint_cb, tensorboard_cb])

# Jupyter Notebook Loadup
%load_ext tensorboard
%tensorboard --logdir=./my_logs --port=6006
```
