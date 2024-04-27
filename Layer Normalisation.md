Layer normalisation is a technique commonly used in deep learning models, including attention models like transformers. It helps to address the problem of internal covariate shift, which can hinder training and performance.

**What is Internal Covariate Shift?**

During training, the distribution of the activations (outputs) of a layer can change significantly. This shift can happen between different layers or even within the same layer during different training epochs. This shifting can make it difficult for the model to learn effectively.

**How Does Layer Normalisation Work?**

Layer normalisation addresses covariate shift by transforming the activations of each layer to have a zero mean and unit variance. This normalisation is applied independently to each feature (channel) in the activation. Here's a simplified overview of the steps involved:

1. **Calculate Mean and Variance:** For each training mini-batch, the mean (µ) and standard deviation (σ) of the layer activations are computed across the feature dimension (i.e., for each channel/neuron).
    
2. **Normalisation:** Each activation value (a) is then normalised using the following formula:
    
    ```
    normalized_a = (a - µ) / √(σ² + ε)
    ```
    
    - ε (epsilon) is a small constant value added to the standard deviation to prevent division by zero.
3. **Scaling and Shifting (Optional):** After normalisation, the activations can optionally be scaled and shifted using learnable parameters γ (gamma) and β (beta). This allows the model to recover the original scale and distribution of the activations if necessary.
    

**Benefits of Layer Normalisation**

Layer normalisation offers several benefits in attention models:

- **Improved Stability:** By normalising activations, layer normalisation helps to stabilise the training process and makes the model less sensitive to the initialisation of weights and learning rates.
- **Faster Training:** Normalisation can accelerate training by alleviating the problem of vanishing or exploding gradients, which can slow down learning.
- **Better Performance:** Layer normalisation can improve the overall performance of the attention model by addressing covariate shift and promoting faster convergence.