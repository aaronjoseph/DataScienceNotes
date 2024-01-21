#dl Non-parametric models do not assume a predefined form for the model. Instead, they determine the model structure based on the data. Here are some examples of non-parametric models:

- Nearest neighbor classifier
- [[Decision Trees]]

### Nearest Neighbor Classifier

The nearest neighbor classifier is a simple algorithm that stores all available cases and classifies new cases based on a similarity measure (e.g., distance functions).

### Procedure

- **Input**: A dataset with labeled examples, and a new query point.
- **Output**: Label for the query point.
- **Steps**:
  1. Measure the distance from the query to all examples in the dataset.
  2. Identify the example with the shortest distance to the query.
  3. Assign the label of this nearest example to the query point.
