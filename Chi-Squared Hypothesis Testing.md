Chi-Squared Hypothesis testing is done for Nominal values. 

Steps

1. First step is to obtain the Average Conversion ratio
2. Then develop the matrix for the Average Conversion
3. Then compute the distance, summing over the cells of the matrix:

   $$
   D = \sum_{\text{cells}} \frac{(O - T)^2}{T}
   $$

4. Here T indicates the expected Population Value and O indicates the real value
	1. The conversion rate from O is used to develop the matrix for T
5. Then apply chi2.sf(D, df=1) on the Above Equation