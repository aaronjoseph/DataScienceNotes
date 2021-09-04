This is the No-Sql variant in GCP eco-system

- Alternative to MongoDB/CouchDB
	- Suited for document data - XML/HTML
- Key-value structure
- Typically not used either for OLTP/OLAP
	- It's key advantage lies in fast lookup on keys, which is the common use case
- Most common use case is the for fast lookup on keys
- `Query execution time depends on size of returned result (not size of data set)`
	- Ideal for "needle in a haystack" type applications       
- This is not meant for write-intensive tasks, but for read-intensive

## Differences & Similarities between RDBMS & DataStore

RDBMS | DataStore
--|--
Similarities | 
Atomic Transaction | Atomic Transaction
Indices for fast lookup | Indices for fast lookup
Some queries use indices - not all | All queries use indices
Query time depend on both size of data set and size of result set | Query time independent of data set, depends on result set alone
Differences | 
Structured relational data | Sturctured hierarchical data (XML,HTML)
Rows stored in Tables | Entities of different in Kinds (think HTML tags)
Rows consist of fields | Entities consist of Properties
Primary keys for unique ID | Keys for unique ID
Rows of table same properties (Schema is strongly enforced) | Entities of a kind can have different properties
Types of all values in a column are the same | Types of different properties with same name in an entity can be different
Joins are supported | Joins are not supported
Filtering on subqueries | No filtering on subqueries
Multiple inequality conditions | Only one inequality filter

## Avoid DataStore When

- Don't use if you need very strong transaction support (OLTP) - OK for basic ACID support though
- Don't use for non-hierarchical or unstructured data - [[BigTable]] is better
- Avoid it for OLAP use cases - Analytics, BI & Data Warehousing - [[BigQuery]] is a better usecase
- Don't use for immutable blobs like movies each >10MB - Use [[Cloud Storage]]
- Avoid if there is lot of writes and updates on the key columns

## When DataStore is to be used

- Use for significant scaling of read performance - to virtually any size
- Use for hierarchical documents with key/value data

## Multi-tenancy

- Seperate data partitions for each client organization
- Can use the same schema for all clients, but vary the values

## Transaction Support

- Transaction Support exists, however, Cloud Spanner cloud be a better alternative

