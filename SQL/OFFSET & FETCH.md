Offset fetch clause implements paging. It returns a page of results from the dataset

```sql
Select * from  table
Order by column_list
offset rows_to_skip ROWS
fetch next rows_to_fetch ROWS ONLY

--- Example
select * from table
order by column
offset 10 rows
fetch next 10 rows only
```