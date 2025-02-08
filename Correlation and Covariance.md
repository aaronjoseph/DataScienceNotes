### Formulae for 
- Correlation - [[Kendall's Tau]], [[Spearman Correlation]]
- Covariance
- Variance
- Standard Deviation

## Formulae

**Correlation coefficient**
$$r = \frac{\sum(x- \bar{x})(y- \bar{y})}{\sqrt{\sum(x- \bar{x})^2(y- \bar{y})^2}} $$

**Covariance**

$$Cov_{xy} = \frac{\sum(x-\bar{x})(y-\bar{y})}{(n-1)} = \frac{\sum{xy} - n\bar{x}\bar{y}}{n-1} $$

**Variance**

$$\sigma^2 =\frac{\sum(\chi-\mu^2)}{N}$$

**Standard Deviation**

$$\sigma = \sqrt{\frac{\sum(x-\bar{x})^2}{n-1}}$$

### Correlation
- Correlation correlates to how well two variables fluctuate together, positive correlation indicates postive change to the other values, which negative correlation indicates the opposite
```py  
# Pandas Corr is useful for this
DF.corr()
```
- Value fluctutes from -1 to 1

### Covariance
- Indicates the strength of the relation
- Not widely used
- Is not range bound like correlation

