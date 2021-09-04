

PCA or Principal Component Analysis is a dimensionality reduction method that transforms large sets of variables into smaller ones with most of the information in the large set.

### Steps in PCA
1. Standardization
This is the first step in the, wherein the variance is contained. PCA is prone to high variance, standardization helps in solving this issue.
2. Covariance Matrix Computation
Covariance Matrix will determine the relationship between multiple independent variables
Covariance matrix for 3 independent variables x,y,z is
$$\begin{bmatrix}
Cov(x,x) & Cov(x,y) & Cov(x,z)\\
Cov(y,x) & Cov(y,y) & Cov(y,z)\\
Cov(z,x) & Cov(z,y) & Cov(z,z)\\
\end{bmatrix}$$

Cov(x,y) = Cov(y,x), Covariance table is the table of summary of correlations between all possible pairs of variables

3. Compute EigenVectors and EigenValues of Covariance Matrix to Identify Principal Components
This is the most important step in the process
- Every Eigenvector has eigenvalue, their number is equal to the number of dimensions
- Eigenvectors and eigenvalues form the basis for PCA, since, Eigenvectors of the covariance matrix are actually the directions of the axes where there is the most amount of variance, which is known as Principal Component

4. Feature Vector
Feature Vector stage, removes features that will result in `dimensionality reduction`

5. Recasting the data along the principal component axes

<iframe border=0 frameborder=0 height=500 width=550  
 
src ="https://twitter.com/Jeande_d/status/1417093660244594688?s=20"</iframe>

