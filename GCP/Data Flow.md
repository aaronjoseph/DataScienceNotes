- Dataflow models the flow of data through a set of transformations
- DAG based representation is used
- Dataflow is modeled on `Apache Beam`
	- Apache Beam is used for both batch and streaming data-parallel processing pipelines
	- It is particularly useful for paralled data processing tasks
- DataFlow is serverless and No-Ops
- It can auto-scale during mid-job

## Cloud Data Flow Streaming Features

Dataflow provides serverless service both for batch and streaming data. Also, allows low-latency data.

`Challenges of Streaming Data`

1. Scalability
2. Fault Tolerance
3. Model - Streaming or Repeated Batch
4. Timing- If data arrives late
5. Aggregation on Unbounded set

> To solve for aggregation on unbounded set, it is preferrable to divide time into windows and obtain average in a given window. [[PubSub]] data have timestamp, it can be used for the windowing


## Types of Trigger

1. Event Time Trigger
	1. Here, based on the AfterWatermark
2. Processing Time Triggers
	1. Processing time triggers
3. AfterCount
	1. Data Driven Trigger

