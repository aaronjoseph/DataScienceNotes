**Consistency** - Every read receives the most recent write or an error
**Availability** - Every request receives a response, without guarentee that it contains the most recent version of the information
**Partition Tolerance** - The system continues to operate despite arbitary partitioning due to network faliures

_Networks aren't reliable, so you'll need to support partition tolerance. You'll need to make a software tradeoff between consistency and availability._

#### CP - consistency and partition tolerance

Waiting for a response from the partitioned node might result in a timeout error. CP is a good choice if your business needs require atomic reads and writes.

#### AP - availability and partition tolerance

Responses return the most readily available version of the data available on any node, which might not be the latest. Writes might take some time to propagate when the partition is resolved.

AP is a good choice if the business needs allow for eventual consistency or when the system needs to continue working despite external errors.