# Feature Cross

#search-eng

## Core Idea

A feature cross represents an interaction between inputs. It allows a linear model to respond differently to combinations even though it remains linear in its engineered features. Crossing usually **increases** representation size; it does not inherently compress information.

For numerical features, $x_1x_2$ is an interaction. For categorical features, a joint category such as `(query_type=brand, exact_brand_match=yes)` can be one-hot encoded. Categorical encoding and crossing are related but different operations.

## Worked Example

Consider $s=b+w_1x_1+w_2x_2+w_{12}x_1x_2$. With $b=w_1=w_2=0$ and $w_{12}=2$, the score is two only when both binary inputs are one. This expresses a combination-specific effect absent from the corresponding additive model without the cross.

## Costs and Pitfalls

Crossing categories with cardinalities a and b can create up to ab combinations. Rare or unseen combinations need a policy. Hashing bounds width but introduces collisions. Trees and neural models can learn some interactions internally, yet an explicit cross can still be useful depending on data and constraints.

## Search Exercise

Cross query intent with price bucket and compare against separate features in [[Logistic Regression]]. Evaluate on unseen queries, inspect sparse combinations, and apply [[L1 and L2 Regularization|regularisation]]. All cross inputs must exist at serving time; see [[Feature Engineering]] and [[Data Leakage]].

## References & Useful Links

- [Google feature crosses](https://developers.google.com/machine-learning/crash-course/categorical-data/feature-crosses) — Primary reference for the explanation above.
