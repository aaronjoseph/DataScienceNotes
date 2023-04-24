1. Prabhat Rastogi

1.  What are the biggest challenges that Novo Bank faces in the small business banking space, and how do you see data science helping to address those challenges?
2. How do you make revenue ?
    
2.  Can you tell me about a recent business problem that Novo Bank faced, and how the data science team helped to solve it?
    
3.  What is the long-term vision for Novo Bank, and how do you see data science contributing to the company's growth and success?
    
4.  How does Novo Bank differentiate itself from other digital banks in the small business banking space, and how does data science play a role in that differentiation?
    
5.  How does Novo Bank use data and analytics to better understand its customers and their needs, and how does this inform product development and marketing strategies?
    
6.  What are some of the key performance indicators (KPIs) that Novo Bank tracks to measure its success, and how does data science help to optimize those KPIs?
    
7.  Can you tell me about a specific project that the data science team has worked on that has had a significant impact on Novo Bank's business operations or bottom line?

Countries

Country, Continent, Population
India, Asia, 1.3B
US, NA, 350M
Nepal, Asia, 30M


Distinct continents where “all countries” individually in that continent have population < 300M

Select distinct(continent) from table
Where continent not in (
(Select continent, country, population  from table
Where pop> 300M))


Select continent, max(population) from table
Group by 1
Having max(p) < 300M



Card_transactions

Txid, userid, amount, timestamp, 
1,1,10,3Jun 2pm…. 0
2,1,25, 3Jun 9pm … 10
3,1,12,5jun 8pm… 0



{sum of amount by user of this transaction in last 24 hrs from this transaction}



Linear  / Logistic

P-values / t-stats

Null Hypothesis : Reject /  don’t ..

Y = ax1 + bx2 + c
B ~ 0 
~ p < 0.05 => “< 5% probability of {what}“

B = 0 ?

—---------------


Growth => Finserv =>CS => Infra |   Ecosystem

Tech
Data  - DE / DS / DA
Product

NSQL / NSL
Deposit Intent
Fraud
ACH 
Check
Card

NS - “High Value”

NSQL; NSQL -> NS; CS - 

14 / 7




