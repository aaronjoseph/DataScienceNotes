Here are a few SQL optimization techniques to start exploring with the basics, the logical order of execution of a query:  
  
FROM (& JOIN): The database will merge the data from all tables, according to the JOINs ON clauses, while also fetching data from the subqueries.  
👉 Try not using nested subqueries within the JOIN tables  
👉 Try not to use complex logic within the JOIN tables  
👉 Try using Filter in JOIN condition instead of WHERE  
  
WHERE: Do not try using aggregates here, the reason this statement fails is that aggregations will be evaluated later in the process  
👉 Try not to filter using functions on top of column values under WHERE clause  
  
GROUP BY:  Not having a GROUP BY clause is like putting all rows in a one huge bucket which we obviously can't make sense of  
👉 Use group for removing duplicates, single queries can use either of the two but group by should always be used when dealing with sub-queries  
  
HAVING: filters out aggregated data that doesn’t meet the criteria  
👉 Try using these to restrict the query output by using some conditions but use where when possible  
  
SELECT: Selects column names, aggregations and subqueries however aggregation functions have already occurred when the grouping took place  
👉 Write table alias before column names to make it easier to identify which columns come from which tables  
👉 Write column names under SELECT instead of getting all columns  
👉 Avoid SELECT DISTINCT and instead use GROUP BY for de-duplication  
  
UNION: Combines the result sets of two queries into one  
👉 Choose UNION DISTINCT vs. UNION ALL which just combines the result sets without applying any duplication check or apply a group by on top of a UNION query  
  
ORDER BY: Sorting takes place once the database has the entire result set ready   
👉 Do not use ORDER BY in subqueries  
  
LIMIT: Used when we would want to discard all rows but a few  
👉 Do not use LIMIT to reduce the query run time or query load as the limit is executed at the very end, thus the whole execution would go on, and then just before the final result, the output gets limited.

---

### Other Best Practices

  
1. Write SQL keywords in capital letters
2. Use table aliases with columns when you are joining multiple tables
3. Never use select *, always mention list of columns in select clause
4. Add useful comments wherever you write complex logic. Avoid too many comments
5. Use joins instead of subqueries when possible for better performance
6. Create CTEs instead of multiple sub queries , it will make your query easy to read
7. Join tables using JOIN keywords instead of writing join condition in where clause for better readability
8. Never use order by in sub queries , It will unnecessary increase runtime
9. If you know there are no duplicates in 2 tables, use UNION ALL instead of UNION for better performance
10. Use EXISTS in place of IN wherever possible
11. Use WHERE instead of HAVING to define filters on non-aggregate fields
12. Avoid wildcards at beginning of predicates (something like '%abc' will cause full table scan to get the results)
13. Considering cardinality within GROUP BY can make it faster (try to consider unique column first in group by list)
14. Get data in temp tables and then execute aggregate/join operations on limited records of large data table