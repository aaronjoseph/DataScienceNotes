Given a word vector, to quantify the similarity between individual words, cosine similarity can be employed. This will help us understand words that are "close" and "far" from one another.

The formulae used here is 

> Cosine_Distance = 1 - Cosine Similarity

Therefore, Cosine_Distance is inversely proportional to Cosine Similarity.
Also, Cosine Similarity concept is used in 
- Recommendation System
- Finding similar words or Documents

### Cosine Similarity for Documents

$$Cosine Similarity = cos(\theta) = \frac{A.B}{||A||*||B||}$$

$$CosineSimilarity \epsilon  [-1,1]$$
Where A & B is the [[TF-IDF| tfidf]] vector of the document