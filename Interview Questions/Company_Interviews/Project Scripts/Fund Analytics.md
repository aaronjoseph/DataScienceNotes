Situation : 

The biggest truth is that there is a big source of noise in the mutual fund industry when it comes to fund selection. With over 10061 funds available in the indian market, a process that can identify funds suited for your needs practically doesn't exist and is a deeply endemic problem. Since mutual funds are purchased based off strong misconception or intellectual faliure, most customers buy into low-performing funds basis mark-to-market.

The absolute need here is to have a fund-selection process that is well differentiated from the competition and is suited to our customers needs. 

For me, it was important early on to think about the fund & customer fit wherein fund returns post investment was quite important. Developing KPI's such as XIRR which will help understand returns on an annulized basis & Sharpe Ratio which is Mean Returns/SD.

Then there is the challenge of approaching fund selection, there is an absolute need to be cognizant of our core philosophy for selecting funds and the principles that we need to abide by whenver the process is followed and the codification of all of it in a document and codebase - for which I was entirely responsible. 

The process of selecting funds is very selective both in technical and fundamental aspects of selection, wherein I learnt the function side of things to master fund selection on the fundamental side of mutual funds wherein I learnt the process from the company CFO, who was kind enough to teach me the intricacies of the financial world. In all the process is about identifying the best fund and one of things that really worked for us is the moving window mean XIRR returns which helped us understand the performance basis the horizon period.  

All in all the entire process was an inward facing and introspective journey. The fund selection process worked phenomenally well for us, infact this may sound crazy however  pre-covid we had 100% positive returns for customers whose first investement was post 90 days of first investment, which I should say is quite phenominal and a testimony to the fact that we nailed Fund Selection and Customer Returns fit. 

The entire analytical approach was done from scratch and we didn't copy any playbook which was in the market and modified over it, the entire process was an amalgamation of analytics and financial know-how to focus on the metrics that mattered to us the most.

Action :

This project boils down to 4 major parts which I handled entirely
- Data Engineering & Analytics & Deployment
- Customer Returns Dashboards
- Fund Selection
- Treasury Fund Selection

### Data Engineering & Analytics & Deployment

I handled data engineering wherein I obtained data from a publically available API. I researched a lot on databases from AWS RDS, Aurora, Athena/Presto, wherein I understood the difference between OLAP and OLTP and made the final decision to use Postgres database, in the process I spent about 20K or $300 dollars  in AWS by accidently leaving AWS aurora instance on, and I learnt how expensive databases can get. I handled DBA for the postgres database, indexed the commonly used columns for performance gains. Also, the tables were desined in the 2nd Normal Form which led to smaller size of the database and better performance.

I also developed codes for correcting data in time-series wherein corrections are applied whenever there are jumps in asset price, so the analysis done over the data doesn't lead to erroneous results. 

Then I corrected the bug for the convergence function used for calculating annualized returns and got it standardized across the team.

I also deveoped code for SMTP mailing which was to be triggred whenever the code fails in the production environment or whenever our customer returns falls below 4 % annualized returns

I also developed stand-alone connector codes. All of facets of code that I just mentioned was structured systematically in Utils file wherein I put all of them in a class as staticmethod so each of it can be invoked as an API within the codebase, making the code-base compact and less faulty. 

The code wasn't implemented in piece-wise fashion and was instead done in a manner such that the code can be scaled for other requirements and the codebase has highest commits within the data science team currently stands at `313` commits. 

I also created codebase to obtain moving window returns analysis which provided the fund performance metrics. I also desined Streamlit app to deploy the fund performance data over app while containerising the entire app within docker.

### Customer Returns Dashboard

While the development was fund selection, the priority for the comany was to drill down on customer level and understand how the returns are at customer level. So I designed a comprehensive dashboard on customer returns

### Fund Selection

Fund selection is the process of using technical and fundamental analysis to select funds for our customer. Technical analysis required heavy analytics to filter for funds.  Some of the key improvements I was redeveloped numerical techniques to simplify cashflow calculation by using the summation of reciprocal of the last cashflow, this technique led to improvement of over 13% in the universe of fund calculation. I also redesigned exponential decay function by using  $(1/T)^{DecayFactor}$ which had a half life of T = 1000  

What worked really well for us was to focus on minimizing standard deviation. Fundamental analysis required reading the scheme documents which required financial understanding to make the final decision

### Tresury Fund Selection 

With my experience in leading fund analytics end to end, I was given the responsibility to monitor the company VC funds invested in Liquid and Ultra-Short funds, wherein the major challenge for us was that asset price information had a time delay and therefore there was a need to develop a monitoring system to evaluate any change in asset prices and trigger emails whenever such cases occur. I also developed a dashboard for this and developed Modern portfolio theory using monte carlo simulation to select funds to be sold/purchased which was done over Streamlit app using docker wherein I also used caching to improve app performance. My tool was used as an aid to make investment decisions in the tune of 48.4 Crores.

### Results

With this project the company was able to actively monitor customer returns which used complex finanacial calculations, the dashboard was completed done from scratch by me

Secondly, with the migration from HDF5 to Postgres I was able to obtain over 15 % quering speed, which improved performace over the apps we deployed

---

Lack of Fund Strategist 

How to hire a fund strategist- lot of shedding and relearning and will take about 6  months before being effective. This has been a lot of work to get the person with the right background and skill-set and we were not successful so far