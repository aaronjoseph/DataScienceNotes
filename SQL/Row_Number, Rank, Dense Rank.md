Rank - In rank function, if there is a tie between two values, the values are same. Also, there is skipping of values

Dense Rank - Same as rank, however, there is no value skip

Row_Number - There is consistency of ranking with no duplicate values


Value | Rank | Dense Rank | Row_Number
---- | ---- | ----- | -----
1.1 | 1 | 1 | 1
1.1 | 1 | 1 | 2 `By Order By Clause`
1.2| 3| 2 | 3
