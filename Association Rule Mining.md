In Association Rule Mining we try to uncover relationships between different items sold by a retailer or find patterns that were not discovered earlier.

The base of Association Rule Mining is based on Maket Basket Analysis. The core idea is to uncover relationships between items so that such products can be placed closely. This is designed to drive more purchase.

A (IF/Antecedent) -> B (Then/Consequent)

In the above relationship, based on occurance of A, B has to occur. Based on the data that is captured, association rule mining can be used to maximise sale.

### Support

Support indicates how frequently the if/then relationship occurs in the dataset 

$$Support = \frac{freq(A,B)}{N}$$

Support can help filter the items that has been bought less frequently. Support indicates the popularity of a product or entity

### Confidence

Confidence indicates the degree to which the if/then relationship actually occurs

$$Confidence(X-->Y) = \frac{supp(X\cup Y)}{freq(supp(X))}$$

### Lift

Lift gives the strength of a rule

$$Lift(X --> Y) = \frac{supp(X \cup Y)}{supp(X)*supp(Y)}$$

If lift >1, then it indicates Y is likely to be bought with X, if it is lift <1, then purchase of Y is less likely

### Confidence

$$Conv(X-->Y) = \frac{1-supp(Y)}{1-conf(X-->Y)}$$

### Apriori Algorithm

Apriori Algorithm uses frequent item sets to generate association rules. It is based on the concept that a subset of a frequent itemset must also be a frequent itemset itself.

Frequent Itemset is an itemset whose support value is greater than a threshold value.

Basically it means,
1. All subsets of a frequent itemset must be frequent
2. Additionally, for any infrequent itemset, all its supersets must be infrequent too

### Steps taken

1. Take the frequency of the occurance of items
2. Remove items that are below the threshold
3. Develop Itemset of combination, order doesn't matter
4. Obtain the occurance of each pair in the transactions
5. Only significant occurance need to be taken that pass the threshold
6. Develop a itemset with 3 pairs


### Pros and Cons of Apriori
- It is easy to understand
- However for large dataset, it will be computationally expensive


### Areas where Association Rule Mining has been used

1. Market Basket Analysis
2. Medical Diagnosis
3. Census Data
4. Protein Sequence

### Libraries

```py
from mlxtend.frequent_patterns import apriori, association_rules

# Frequent Itemset
frequent_itemset = apriori(basket_sets, min_support=0.07, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift",min_threshold=1)
```