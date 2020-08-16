Windowing Function can be used on 

Aggeration - Avg, Sum, Sum, Min, Max etc
Ranking Function - Rank, Dense_Rank, Row_Number
Analytical Function - Lead, Lag, First_Value, Last_Value

Over Clause defines the partitioning and ordering of rows.  Over takes 3 arguments
1. Order By  - Ordering specification
2. Partition By - Criteria to partition by
3. Rows or range Clause - Specifiying the start and points
	1. Default specification of the query will be 
 
 ```sql 
 Range between Unbounded preceeding and current row
 ```

Syntax, using all the parameters

```sql
select *, SUM(col_name) over (order by col_name_1 partition by col_name2 rows between unbounded preceeding and unbounded following)

-- Here for the rows over unbounded preceeding and unbounded following can be modified as 
rows between 1 preceeding and 1 following
rows between current row and 1 following
```