- Relational database
- Cloud SQL is open source
- Cloud Spanner is proprietary
- Both support ACID Properties - relevant for OLTP (transaction processing)
- Cloud Spanner supports ACID++
- OLTP needs strict write consistency, OLAP does not

## Cloud SQL vs Cloud Spanner

- Cloud Spanner is Google Proprietary & more advanced that CloudSQL
- Cloud Spanner supports "[[Horizontal & Vertical Scaling|horizontal scaling]]"

## [[BigQuery]] Vs Cloud SQL, Cloud Spanner
- Cloud SQL & Cloud Spanner are RDBMs, and due to its stringent write consistencies, it cannot really scale up to BigData level
- If your data is massive and unstructured, use BigQuery
- However, if the data is quite small and is very structured, use Cloud SQL & Cloud Spanner

## Cloud SQL

- CloudSQL is not `serverless`
- `High Availability Configuration`
	- This means, the DB has a failover replica
	- The failover replica must be in a different zone than the original instance, also called master
	- All changes made to the data on the master, including to user tables, are replicated to the failover replica using semisynchronous replication	

## Cloud Spanner

- Cloud Spanner is Google proprietary, more advanced than Cloud SQL
- Cloud Spanner offers "horizontal scaling" - bigger data, more instances, replication
- Cloud Spanner should be used when
	- Need high availability
	- Strong consistency
	- `Transactional reads and writes (It's write optimized)`
- Avoid using Cloud Spanner for
	- Data is not relatoinal, or not even structured
	- Want an open source RDBMS
	- Strong consistency and availability is overkill
- There is subtle similarity with [[HBase]] and therefore hotspotting is an issue in Cloud Spanner
- `Hotspotting` is the occurance of a node servicing all the read or write requests, despite having multiple nodes
	- In the [[HBase]] architecture, all the read and write requests are based on the row key. The row key is instrumental for HBase to be able to take advantage of all regions equally
	- Avoinding hotspotting
		- Do not use monotonically increasing values, else wirtes will be on same locations
		- Use hash of key value - this will share data in different shards evenly
- Cloud spanner is preferred for mission critical use cases, and should be deployed in locations where you expect maximum traffic 