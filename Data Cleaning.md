### Shuffling the Data

Data can be shuffled as follows 

```py
import numpy as np

# For illustration only. Sklearn has train_test_split()
def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]
```

```py
from sklearn.model_selection import train_test_split

train_set, test_set = train_test_split(DF, test_size=0.2, random_state=42)
```