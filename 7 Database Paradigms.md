There are 7 types of databases

### Key-Value Database

- Popular Database in this space are
	- Redis
	- MemcacheDB
- This works like Javascript Object or Python Dictionary
- This database is stored on Machine Memory as against Disk Memory
	- Therefore this makes the database faster
- This doesn't allow for queries or join
	- Hence the data modeling options are very limited
- This is used for real-time use-cases
	- However, this is generally formed over some form of persistent data layers

### Wide-Column Database

- Examples
	- Cassandra
	- Apache [[HBase]]
- This works on the Key-value pair idea, and adds another dimension to the value part
- Unlike Relational database, this lacks schema
	- However, querying is possible using something called CQL
	- This database is easier to scale up
	- And can be replicated across multiple nodes, horizontally
- Best for
	- Time Series Data
	- Historical Records
	- High Write and Low Read

### Document Based Database

- Here, each document is a container for key-value pairs
- It is unstructured and don't require a schema
- Documents are grouped 
- It is general purpose
- Ideal when the structure of the data cannot be understood
- Not ideal for graphs

### Relational Database

- Its one of the most popular database
- Developed by Ted Codd
- Uses SQL

### Graph Database

- Query can be concise and simpler
-  Shows relationship between elements
- Useful for 
	- Financial Use case - finding fraud
	- Internal Knowledge Graph
	- Recommendation Engine

### Search Database

- Example
	- Solr
	- Lucent
- Similar to document oriented database, however, the search database will go through the database and index the data
	- This makes search faster
	- However the overheads are quite high for such database

### Multi-Model Database

- Example
	- Fauna DB
- It goes about 3 paradims
	- Graph
	- Document
	- Relational DB
- It is ACID compliant  
- You are not worried about the data modeling
- No need to provision the cloud infrastructure