Given a word vector, to quantify the similarity between individual words, cosine similarity can be employed. This will help us understand words that are "close" and "far" from one another.
### Cosine Similarity for Documents

$$Cosine Similarity = cos(\theta) = \frac{A.B}{||A||*||B||}$$
The dot product of two vectors $(A = [a_1, a_2, \dots, a_n])$ and $(B = [b_1, b_2, \dots, b_n])$ is defined as: 
$$[ A \cdot B = a_1 \cdot b_1 + a_2 \cdot b_2 + \dots + a_n \cdot b_n]$$
Here, $||A||$ is Norm 2 (Euclidean Norm)
$$||A||_2 = \sqrt{a_1^2 + a_2^2 + \dots + a_n^2}$$
$$CosineSimilarity \epsilon  [-1,1]$$
Where A & B is the [[TF-IDF| tfidf]] vector of the document
### **Applications of Cosine Similarity**

1. **Recommendation Systems**:
    - **Content-Based Filtering**: Cosine similarity is used to recommend items (e.g., movies, products, or articles) that are similar to items the user has already interacted with.
2. **Finding Similar Words**:
    - In natural language processing, cosine similarity is used to find words that have similar meanings based on their word embeddings.
3. **Document Similarity**:
    - Cosine similarity is also used to compare documents based on their word embeddings or term frequency vectors.
    **Example**: Two documents about technology may have high cosine similarity because their word vectors (or term frequency vectors) are close, indicating they discuss similar topics.

### Cosine Distance

Therefore, Cosine_Distance is inversely proportional to Cosine Similarity.
Also, Cosine Similarity concept is used in 
- Recommendation System
- Finding similar words or Documents
 
$$\text{Cosine Distance} = 1 - \text{Cosine Similarity}$$
- If the cosine similarity is 1 (indicating identical vectors), the cosine distance will be 0.
- If the cosine similarity is 0 (indicating completely dissimilar vectors), the cosine distance will be 1.

**Interpretation**:
- **Lower cosine distance**: Vectors are closer, meaning the words are semantically similar.
- **Higher cosine distance**: Vectors are farther apart, meaning the words are less similar or have different meanings.