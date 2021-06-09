Hive is based out of [[Hadoop]] ecosystem.
This provides SQL interface to [[Hadoop]] and works over Hadoop. This bridge to Hadoop is critical for folks who don't have exposure to JAVA

Hive is preferred for batch processing task and is not ideal for real-time processing.

`Hive Metastore` is the bridge between Hive tables and HDFS, when the results from HIVE comes in, it comes in a table format, which in reality are files. This is acheived by using the HIVE Metastore.

## Hive vs RDBMS

Hive | RDBMS
---|---
Large Datasets | Small Datasets
Parallel computations | Serial computations
High Latency | Low Latency
Read Operations | Read/Write Operations
Not ACID compliant by default | ACID compliant
HiveQL | SQL

> Hive has latency issue due to records not being indexed. And therefore the data cannot be accessed quickly. Additionally, for a small amount of data to be accessed, you still need to account for the overhead of mapreduce, which means the entire infrastructure needs to run through

## Partitioning and Bucketing

- Partitioning and Bucketing are ways of spliting data into smaller & manageable parts.
- This helps with performance optimization

Partitioning
- In partitioning, data may be naturally split into logical units
- Here, each unit of data split will be stored in different directory
	- This has significant improvement will lead to simpler lookup since the data is stored in known directories
	- However, the split in this case, may lead to differing size of the split, since each unit will have varying amount of data

Bucketing
- In bucketing, the data is split based on size, since each split should be of the same size
- Split of a specific size has performance advantage