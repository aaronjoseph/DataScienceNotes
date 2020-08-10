Difference between SQL and NoSQL

SQL | NoSQL
---- | ----
 Scheme is not flexible | NoSQL Schema is flexible
 Addition of column is an expensive operation, since there are locks to be maintained | Addition of columns are very straightforward since Scheme design is simple and flexible `Scheme can be easily changed or updated on the fly`
 Read scaling is high, can handle higher volumes of read operation `Read Optimized` | Same, advantages here are that NoSQL doesn't have to follow ACID properties and therefore can speed up due to it
 Write scaling maynot be as fast as NoSql | Write scaling is very fast `Write Optimized`
 Designed for updates | Not built for updates
 Consistency is not a problem (ACID) | Consistency is a problem
 Implicit information about relation is well understood | Information of relation isn't part of the design
 Joins are easy, SQL systems are designed for joins | Joins are hard - Since every block of relevant data has to be searched