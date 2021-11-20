<a href ="https://www.youtube.com/watch?v=DEuvGh4ZwaY&feature=youtu.be"> Link</a>
[[Churn Analysis]]

Steps to improve the performance of the model

### Typical Experiments to increase CV & LB with

- Preprocessing & [[Feature Engineering]]
	- `Correlation` - Find features that are highly correlated to the target variable
	- `Completion or Imputing` [[Imputing Missing Values]] Can be done to fix missing data
	- `Creating of New Features/ Feature Engineering` - Adding additional  features
	-  Removal of Data that are irrelevent - This will speed up the analysis
	- First round of exploration does not have to be absolutely thorough; the point is to start off on the right foot and quickly gain insights that will help you get a first reasonably good prototype. But this is an iterative process: once you get a prototype up and running, you can analyze its output to gain more insights and come back to this exploration step
	- Some models are prone to repeated data, and it is important to shuffle the data
	- `Data Wrangling/Data Munging` - Process of transforming the data for the purpose of analysis
- Data Augmentation & External Data
	- `Data Augmentation` is the process of modifying the exisiting data to make the algorithm more robust
- Model Architecture & Different loss function 
 >[[Transfer Learning]] : Can be used for model Architecture. Ideally it is good to go with the Model with lower parameters so the training is faster 
- Training Schedule, Optimizer
- Postprocessing
> Herein, you can do improvements by leveraging the existing model over the small datasets. This way you can see high performance over the existing model

### Tensorflow Code to use GPU's Dynamically
```py
os.environ["CUDA_VISIBLE_DEVICES"]="0"
gpus = tf.config.list_physical_devices('GPU'); print(gpus)
if len(gpus)==1: strategy = tf.distribute.OneDeviceStrategy(device="/gpu:0")
else: strategy = tf.distribute.MirroredStrategy()

# Enable Mixed Precision
# This speeds up the computation much further
# Allows more memory to be stored on GPU's as well
tf.config.optimizer.set_experimental_options({'auto_mixed_precision':True})
```