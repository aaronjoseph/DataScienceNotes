
https://www.geeksforgeeks.org/k-nearest-neighbours/

### **K-Nearest Neighbours (KNN)**

- **KNN** is a **lazy learning, non-parametric** algorithm used for **classification and regression**.
- It makes predictions based on the **majority class** (for classification) or the **average value** (for regression) of its **K nearest neighbours**.

### **Key Concepts**

- **Distance Metrics:**
    - Commonly used distances:
        - **Euclidean Distance** ($d = \sqrt{\sum (x_i - y_i)^2}$)
        - **Manhattan Distance**
        - **Minkowski Distance**
- **Choice of K:**
    - A **small K** (e.g., K=1) → High variance, sensitive to noise.
    - A **large K** → More generalised, but may blur decision boundaries.
    - **Optimal K** is often chosen via **cross-validation**.
- **Lazy Learning:**
    - KNN **stores** all training data and makes predictions **only at query time**.
- **Feature Scaling is Important:**
    - KNN is **sensitive** to feature magnitudes, so **normalisation** or **standardisation** is needed.

### **Pros and Cons**

✅ **Advantages:**
- Simple to understand and implement.
- Works well with small datasets.
- No explicit training phase (lazy learning).
❌ **Disadvantages:**
- Computationally expensive for large datasets.
- Requires efficient memory storage.
- Performance is affected by irrelevant or redundant features.

### **Use Cases**
- Pattern recognition
- Recommender systems
- Anomaly detection
- Image classification