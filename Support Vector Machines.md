[[Classification Algorithms]]

### Support Vector Machine (SVM)
- **SVM (Support Vector Machine)** is a versatile algorithm used for:
    - **Linear and non-linear classification**
    - **Regression**
    - **Outlier detection**
- **Feature Scaling Importance:**
    - SVMs are **sensitive** to the scale of input features.
    - **Feature scaling** (e.g., standardisation or normalisation) is **necessary** before training to ensure optimal performance.

### Nonlinear SVM Classifier
- A **nonlinear SVM classifier** can be implemented using the **`PolynomialFeatures`** library from Scikit-Learn (`sklearn`).
- This approach allows SVM to **map data to higher dimensions**, making it suitable for **complex decision boundaries**.

### Support Vector Concept
- **Support vectors** are **key data points** that define the **decision boundary**.
- They can **support** different aspects of the classification model, such as:
    - **Sides** (margins of the decision boundary)
    - **Top** (in higher-dimensional space, shaping the boundary)

