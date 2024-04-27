[[Imbalanced Classification]]
There are quite a few metrics that are used commonly used for testing the performance of a model

---
ROC

Most classifiers use probability to distribute samples into classes. In most cases, 0.5 is taken as the thereshold. The choice of threshold may not be the best , hence here, the ROC comes into play and is the plot of TPR (Sensitivity/Recall) and FPR (1-TPR). This is useful in understanding the binary classifier.

- `AUC & ROC` - Area under the curve/ Receiver Operator Characteristics
- AUC/ ROC is used for classification problems [Binary Classifiers]
- ROC is the probability curve & AUC represents degree or measures of separability
- The plot is plotted with TPR vs FPR as shown below

![[AUC_ROC.png]]
	
![[Confusion_Matrix.png]]
- TPR (True Positive Rate) / Recall / Sensitivity 
$$True Positive Rate / Recall / Sensitivity =\frac{True Positive}{True Positive+False Negative}$$

- Precision 
$$Precision =\frac{True Positive}{True Positive+False Positive}$$

```py
# Precision & Recall
from sklearn.metrics import precision_score, recall_score
precision_score(Actual,Prediction)
recall_score(Actual,Precision)
```

- Specificity
$$Specificity = \frac{True Negative}{True Negative + False Positive}$$

- False Positive Rate
$$ False  Rate = \frac{False Positive}{True Negative + False Positive} = 1- Specificity$$

- F1 Score/ F Beta Score
- Also, is the harmonic mean of Precision and Recall
 $$ F1 Score = 2*\frac{Precision*Recall}{Precision+Recall} $$
 
 > Type I Error : `False Positive` 
 > Type II Error : `False Negative` 
 > Type I Error is more serious than Type II Error

Type I error is changing your mind when you shouldn't
Type II error is not changing your mind when you should
Type III error occurs when researches provide the right answer to the wrong question

```py
from sklearn.metrics import confusion_matrix
confusion_matix(Actual_Data, Predicted_Data)
```

Output of Sklearn Matrix

State | Negative Prediction | Positive Prediction
------ | ------| ------
**Negative Class** | True Negative | False Negative
**Positive Class**| False Positive | True Positive

---

AUC Value | Indication
------------ | ------------
1 | High Accuracy 
0 | Worst Measure of seperatibitily - It is giving the opposite class
0.5 | Model has no class seperation

>Sensitivity & Specificity are inversely proportional to each other
>TRP & FPR are directly proportional to each other

---

Using F1 & Accuracy

> F1 should be used when not making mistake is quite important [1-0, 1 is good, 0 is bad]
> Accuracy should be used when models goal is to optimize performance
> F1 Score is used for imbalanced data sets
> Accuracy is relevant for balanced data sets

---

Precision-Recall Tradeoff

In Ideal senario, both Precision & Recall can get a value of 1, however in most practical situation, due to noise, the datasets are not perfectly seperatable. There will be cases of positive classes in close proximity to the negative class and vice-versa.  

`Decision Boundary` - boundary based of which classification is made as to which class a variable belongs to

The decision boundary can be adjusted to either increase or decrease recall/precision and the changes are negatively correlated

`Precision Focused` - Here the premise is that you dont want high cases of false-positive

`Recall Focused` - Here even if negative cases comes up in the prediction, we really don't care about it