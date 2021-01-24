### Pointers
- Generative Statistical Model
- Allows sets of observations to be explained by unobserved groups that explain why some parts of the data are similar
	- If obervations are words collected into documents
- It posits that each document is a mixuture of a small number of topics and that each words presence is attributable to one of the document's topics
- In LDA, each document may be viewed as a mixture of various topics where each document is considered to have a set of topics that are assigned to it via LDA
- LDA the topic distribution is assumed to have a sparse Dirichlet prior. The sparse Dirichlet priors encode the intuition that documents cover only a small set of topics and that topics use only a small set of words frequently

> Each document is assumed to be characterized by a particular set of topics. Each topic is assumed to be characterized by a particular set of words.
---

- LDA is a [[Topic Modeling| topic model]] that generates topics based on word frequency from a set of documents
- LDA is useful for finding reasonably accurate mixtures of topics within a given document

> LDA has very minute difference in terms of how they treat per-document distribution w.r.t. `LSA`
---

### LDA - Naming
**Latent**: This refers to everything that we don’t know a priori and are hidden in the data. Here, the themes or topics that document consists of are unknown, but they are believed to be present as the text is generated based on those topics.

**Dirichlet:** It is a ‘distribution of distributions’. Yes, you read it right. But what does this mean? Let’s think about this with the help of an example. Let’s suppose there is a machine that produces dice and we can control whether the machine will always produce a dice with equal weight to all sides, or will there be any bias for some sides. So, the machine producing dice is a distribution as it is producing dice of different types. Also, we know that the dice itself is a distribution as we get multiple values when we roll a dice. This is what it means to be a distribution of distributions and this is what Dirichlet is. Here, in the context of topic modeling, the Dirichlet is the distribution of topics in documents and distribution of words in the topic. It might not be very clear at this point of time, but it’s fine as we will look at it in more detail in a while.

**Allocation**: This means that once we have Dirichlet, we will allocate topics to the documents and words of the document to topics.

---

There are two matrices

$$\theta_{td} = P(t|d)$$ 

Which is the probability distribution of topics in documents

$$\phi_{wt} = P(w|t)$$ 

Which is the probability of words in topics

Now, the probability of a word given document as,

$$P(w|D) = \sum_{t\epsilon T} p(w|t,d) P(t|d)$$

Here, 

If we assume conditional independence, we have 

$$P(w|t,d) = P(w|t)$$

Therefore

$$P(w|D) = \sum_{t=1}^{T} p(w|t) P(t|d) = \phi_{wt} \theta_{td}$$

> Here, we decompose the probability distribution matrix of word in document in two matrices consisting of distribution of topic in a document and distribution of words in a topic

- Dirichlet parameter controls if all the words have same probability in a topic or will that topic have an extreme bias towards some words. 
- Same intuition is for distribution of topics in a document.

### Steps to be taken 

1. Randomly choose a topic from the distribution of topics in a document based on their assigned weights

2. Next, based on the distribution of words for the chosen topic, select a word at random and put it in the document

3. Repeat this step for the entire document

> Therefore, what we are doing here, is we are trying to maximize the likelihood of our data given these two matrices

To identify the correct weights, [[Gibbs Sampling]] is used.