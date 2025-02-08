**Loss functions** are used to gauge the error between the predicted output $\hat{y}$ and actual output $y$. A loss function indicates how far the algorithm model is from realising the expected outcome. 
$$L(y, \hat{y}) = (y - \hat{y})^2$$

**Cost functions** represents the average of loss function across the entire dataset.
$$J(\theta) = \frac{1}{n} \sum_{i=1}^{n} L(y_i, \hat{y}_i)$$

![[Cross Entropy Loss]]
