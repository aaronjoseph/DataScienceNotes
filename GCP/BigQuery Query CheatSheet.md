List of optimization that can be done when using [[BigQuery]]

- Don't use `select *` 
	- Adding columns makes it slower
- Some built in functions are faster than others
	- APPROX_COUNT_DISTINCT is faster than COUNT(DISTINCT)
- Make use of `WHERE` as much as possible
- Dont use `ORDER BY` in With or Sub-queries, do it in the very last
- `PUT the larger table on the left` - Join
- Low cardinality is faster than high cardinality
- Use partition table for easier search