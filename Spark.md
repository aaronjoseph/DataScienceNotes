[[Spark DAG & Tungsten]], [[Spark Architecture]]

Apache Spark offers several advantages over Hadoop [[MapReduce]], making it a preferred choice for many big data processing tasks:

1. **Performance:**
   - **In-Memory Processing:** Spark processes data in memory, significantly reducing the time spent on disk I/O operations. This approach allows Spark to run applications up to 100 times faster in memory and 10 times faster on disk compared to Hadoop MapReduce, which relies heavily on disk storage for intermediate data. 
2. **Ease of Use:**
   - **High-Level APIs:** Spark provides user-friendly APIs in Java, Scala, Python, and R, simplifying the development process. In contrast, Hadoop MapReduce requires developers to write complex code, often in Java, making it less accessible. 
3. **Versatility:**
   - **Unified Engine:** Spark supports various data processing tasks, including batch processing, real-time streaming, machine learning, and graph processing, all within a single framework. Hadoop MapReduce is primarily designed for batch processing, necessitating additional tools for other tasks. 
4. **Real-Time Processing:**
   - **Stream Processing:** Spark's Structured Streaming enables real-time data processing, making it suitable for applications requiring immediate insights. Hadoop MapReduce lacks native support for real-time processing. 
5. **Fault Tolerance:**
   - **Resilient Distributed Datasets (RDDs):** Spark's RDDs provide fault tolerance by tracking data lineage, allowing for efficient recovery from failures without restarting the entire process. 
   - Key Components of RDD
	1. **Dependencies:**
	    - **Definition:** Dependencies specify how an RDD is constructed from its inputs.
	    - **Resiliency:** If needed, Spark can recreate an RDD using its dependencies and replicate the operations on it. This is the core reason RDDs are **resilient**.
	    - **Purpose:** Ensures fault tolerance by providing a lineage of transformations.
	2. **Partitions (with locality information):**
	    - **Definition:** Partitions are logical chunks of data that Spark processes in parallel.
	    - **Parallelism:** By dividing data into partitions, Spark enables parallel computation across executors.
	    - **Locality Optimisation:** In cases like reading from HDFS, Spark uses locality information to assign tasks to executors near the data, reducing network overhead and improving performance.
	3. **Compute Function (`Partition => Iterator[T]`):**
	    - **Definition:** Each RDD has a compute function that takes a partition and produces an iterator of elements (`Iterator[T]`).
	    - **Purpose:** Defines the logic for processing the data stored in each partition.
	    - **Output:** The iterator contains the transformed data for that partition.

While Hadoop MapReduce remains effective for certain batch processing tasks, Spark's enhanced performance, usability, and versatility make it a more robust solution for a wide range of big data applications. 

---

## Apache Spark Architecture

**Key Components**

**1. Spark Driver**

The **Spark Driver** is the central coordinator of a Spark application. It is responsible for:
- Converting user code into executable tasks.
- Distributing these tasks across the cluster.
- Managing the execution of tasks.

The Driver maintains information about the application’s status and collaborates with the cluster manager to allocate resources.

**2. Spark Executors**

**Executors** are worker processes launched on each node of the cluster. Their responsibilities include:
- Executing code assigned by the Driver.
- Reporting the status of computation back to the Driver.
- Storing data for in-memory processing.

Each application has its own set of Executors, which remain active for the duration of the application, ensuring data isolation and consistency.

**3. Cluster Manager**

The **Cluster Manager** oversees resource allocation across the cluster. Spark can integrate with various cluster managers, including:
- **Standalone**: Spark’s built-in cluster manager.
- **Apache Hadoop YARN**: Resource manager for Hadoop clusters.
- **Apache Mesos**: General-purpose cluster manager.
- **Kubernetes**: Container orchestration platform.

The choice of cluster manager dictates how resources like CPU and memory are allocated to Spark applications.

---

## Reasons why Hadoop went out of Favour

| **Aspect**                       | **Hadoop (MapReduce)**                                | **Spark**                                                              | **Why Spark Wins?**                                         |
| -------------------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------- |
| **Processing Speed**             | Disk-based; slower data processing                    | In-memory computation; significantly faster                            | Faster results and lower latency                            |
| **Ease of Use**                  | Complex and verbose APIs                              | Simpler, user-friendly APIs (e.g., DataFrames, Spark SQL)              | Easier learning curve and productivity boost                |
| **Real-Time Processing**         | Primarily batch processing, limited real-time support | Native support for real-time and streaming analytics                   | Supports a broader range of use cases (batch and streaming) |
| **Multi-language Support**       | Mostly Java-centric                                   | Multi-language: Java, Scala, Python, R                                 | Greater flexibility and developer adoption                  |
| **Advanced Libraries**           | Limited built-in advanced analytics libraries         | Rich set of libraries (MLlib, GraphX, Spark SQL, Structured Streaming) | Provides comprehensive analytics capabilities               |
| **Interactive Queries**          | Poor support for interactive analysis                 | Strong interactive support (e.g., Spark SQL, notebooks)                | Supports interactive analytics and exploration              |
| **Fault Tolerance & Efficiency** | Fault-tolerant but requires frequent disk writes      | Fault-tolerant with optimized execution plans                          | Efficient, optimized resource use                           |
| **Community & Ecosystem**        | Mature but declining community growth                 | Active, growing community with frequent updates                        | Better future-proofing and feature evolution                |
