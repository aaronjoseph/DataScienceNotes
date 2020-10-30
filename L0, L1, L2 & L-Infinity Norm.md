`Norm` - Refers to total length of all vectors in a space

### L0 Norm

L0 Norm is not a norm. It refers to total number of non-zero elements in a vector space.

Consider (0,3), (0,0) -> L0 Norm is 1. Since there is only 1 non-zero element.

Consider the scenario of userid and password

UserID | Password | L0 Norm
---|---|---
Correct UserID | Correct PWD | 0
Correct UserID | Incorrect PWD | 1
Incorrect UserID | Incorrect PWD	| 2



### L1 Norm

Also referred to as `Manhattan Distance or Taxicab norm`

L1 norm is caluclated as follows
$$||x||_1 = |x|+|y|$$

### L2 Norm

Commonly referred to as `Euclidean distance`

It is the shortest distance to go from one point to another

$$||x||^2 = |x|^2+|y|^2$$

### L-P Norm

Commonly referred to as `Euclidean distance`

It is the shortest distance to go from one point to another

$$||x||^P = |x|^P+|y|^P$$



### L-$\infty$ Norm

Consider the vector [10,-11,20],
L$\infty$ will be 11. 