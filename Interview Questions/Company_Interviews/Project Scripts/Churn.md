The biggest predictor of success for any startup or an organisation is the ability to retentin their customers. The other factor that could be looked into are NPS or DAU/MAU, which will also determine the growth of the company.

Companies can always buy growth by means of paid marketing through social media marketing or Google Ad sense. However the general consensus is that it doesn't work in the long run. The company may get into a vicious cycle to keep buying growth to maintain the flow of new customers and could inevitably lead to lower focus on product and can cause the product to get worse over time.

> Cost of getting new customer is often more expensive than retaining the existing customers

Types of Churn
- `Voluntary Churn` - Here the customer switches out to competitor
- `Involuntary Churn` - Inability to pay up and therefore leaves the platform

> Churn analysis is the process of identifying the propensity of risk to exit


For instance at FundsIndia the marketing spend was at 50 Lakhs per month on an average to put this in perspective, what I have learnt from SEO engineers Amazon has spent over 2 Crores a day for Google Adwords alone, so it is a hyper-competitive space

Hence some of the major questions that we needed to get answers on were
1. What were the major factors that correlated to Churn
2. What was the average life-span of customers who came in via Paid Marketing vs Organic Search
3. What percentage of Orgaic and Non-Organic customers finally reached breakeven?
4. What was the biggest driver of growth despite high churn rate, wherein we could narrowly focus

Feature Set
1. Customer Platform Age in days- Outliers
2. No of Sub-Subscriptions
3. Customer Age - Outliers
4. Amount Invested
5. Absolute Return
6. XIRR
7. Equity Proportion
8. Debt Proportion
9. Is_Stock_Holder_Data
10. Avg_Montly_Inflow/Account
11. Avg_Montly_Inflow/Subscriptions
12. Organic/Inorganic
13. InOrganic_Is_FB
14. Quora
15. Google_Ad_Sense
16. No_of_SIP
17. No_of_Lumpsum
18. Avg_Sip_Year
19. Avg_Lump_Year
20. %Sip/All
21. %Lump/All
22. First Trx Value
23. Number of Logins

--- 

Outlier Detection
Outliers were detected for Age of customer and Platform age due to error in capturing data, these observations were replaced by mean values,as all of them were pointing to 1900-01-01

--- 

Suggested Course of Action
1. To reduce spending on FB and Quora for inorganic growth
2. From the analysis, what was observed from RF feature importance, major factors for churn were mostly due to 
	1. Low SIP Trx
	2. XIRR returns
	3. High Equity Portfolio 
3. Focus on recommending select funds at signup to simplyfy the fund selection process
4. To focus on younger customers, firstly 70% of the new customers were above the age of 30, younger customers are generally cash-strapped, however, can bring in revenue in the long run, this is because the average age of FundsIndia customer stood at 49 (Weighted by AUM), average age of India at the time was 28.75
5. Focus on customers with high first inflow, amount of 10,000 rupees in the first 30 days since first transaction, also what was observed was customers with SIP amount of 1000 ruppees didn't contribute much to the 