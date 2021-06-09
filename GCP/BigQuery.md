- BigQuery is Fully managed, no server/serverless , no resources deployed
- Bigquery semantically maps to [[Hive]] technology
	- However it is faster than Hive in terms of giving outputs
	- This is due to the use of Columnar data storage format, which is proprietary as well
	- Therefore Bigquery has differences compared to Hive, `this has to do with the implementation details where BigQuery differs`
- However, Bigquery's latency is higher than [[BigTable]] & [[DataStore]]
- No ACID properties, cannot be used for transaction processing (OLTP)
- Great for analytics/business intelligence/data warehouse (OLAP)
- Dataset = Set of tables and views
	- Table must belong to dataset
	- Tables contains records with rows and columns
- Dataset must belong to a project, so as to be billed

> BigQuery is a columnar DB, so if you reduce the amount of columns in the query, the amount of data processed reduces as well, thereby reducing the query cost. `It doesn't depend on the where condition of the query`

## Table Schema 

- Can be specified at creation time
- Can also specify schema during initial load
- Can update schema later on as well

## Schema Autodetection

- BigQuery selects a random file in the data source and scans upto 100 rows of data to use as a representative sample
- Then examines each field and attemps to assign a data type to that field based on the values in the sample
- Big query can convert data from Cloud Datastore backup files to BigQuery Data

## Querying and Viewing

The different ways interacting with data in BigQuery
- Interactive Queries
- Batch Queries
- Views
- Partitioned Tables

## Interactive Queries

- Default mode - the query is executed as soon as possible
- Use of interactive queries counts towards daily/concurrent usage limits

## Batch Queries

- BigQuery will schedule this form of query whenever possible (idle resources)
- Don't count towards limit on concurrent usage, but on daily usage
- If not started within 24 hours, BQ will convert this into interactive query

## Views

- BigQuery views are logical, not materialised
- Underlying query will execute each time view is accessed
- Billing will happen accordingly
- Can't assign access control - based on user running view
- Can create authorised view : Share query results with groups without giving read access to underlying data 
- Can give row-level permissions to different users within same view
- Can't export data from a view
- Can't use JSON API to retrieve data
- Can't mix standard and legacy SQL
- No user-defined functions allowed
- No wildcard table references allowed
- Limit of 1000 authorised views per dataset

## Partitioned Tables

- Special table where data is partitioned by you
- No need to create partitions manually or programmatically
- Manual partitions - performance degrades
- Limit of 1000 tables per query does not apply
- Date partitioned tables offered by BigQuery
- Need to declare tablee as partitioned at ceration time
- No need to specity schema (can do while loading data)
- BigQuery automatically creates date partitions 
	
---

## Query Plan Explanation

- In the web UI, click on "Explanation"

## Slots 

- Unit of Computational capacity needed to run queries 
- Bigquery calculates on basis of query size, complexity
- Usually default slots sufficient
- Might need to be expanded for very large, complex queries
- Slots are subject to quota policies
- Can use StackDriver Monitoring to track slot usage