Light GBM is a gradient boosting framework that uses tree based learning algorithm.

Light GBM grows tree vertically while other tree based models grows trees horizontally. Light GBM grows tree leaf-wise while other algorithm grows level wise. It will choose the leaf with max delta loss to grow.  When growing the same leaf, leaf-wise algorithm can reduce more loss than a level-wise algorithm.

Light GBM advantages
- Like the name suggests, it is light (has higher speed)
- Light GBM can hanle the large size of data
- Takes lower memory to run

> Light GBM cannot work well with small datasets, since it will overfit the data

Control Parameters

```py
import lightgbm as lgb
```

- `max_depth` Describes the max depth of tree. This can handle model overfitting
- `min_data_in_leaf` Minimum number of the records a leaf may have. The default value is 20, optimum value. It is also used to deal over-fitting
- `feature_fraction`  Used when your boosting is random forest
- `bagging_fraction` Specifies the fraction of data to be used for each iteration and is generally used to speed up the training and avoid overfitting
- `early_stopping_round` This parameter can help you speed up your analysis
- `lambda` Specifies regularization
- `min_gain_to_split` Minimum gain to make a split
- `max_cat_group` when the number of category is large, finding the split point on it is easily over-fitting

