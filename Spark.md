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
	    - **Locality Optimization:** In cases like reading from HDFS, Spark uses locality information to assign tasks to executors near the data, reducing network overhead and improving performance.
	3. **Compute Function (`Partition => Iterator[T]`):**
	    - **Definition:** Each RDD has a compute function that takes a partition and produces an iterator of elements (`Iterator[T]`).
	    - **Purpose:** Defines the logic for processing the data stored in each partition.
	    - **Output:** The iterator contains the transformed data for that partition.

While Hadoop MapReduce remains effective for certain batch processing tasks, Spark's enhanced performance, usability, and versatility make it a more robust solution for a wide range of big data applications. 

---

### Key Spark Terminology

**Spark Session** - The main entry point to interact with Spark functionalities, including DataFrame and Dataset APIs. It allows you to use Spark's features programmatically. In an interactive shell, Spark automatically creates a `SparkSession`, while in a Spark application, you need to create it manually.

**Spark Driver** - The Spark Driver is the central coordinator of a Spark Application. It is responsible for converting the user's code into executable tasks, distributing them across the cluster, and managing their execution. The Driver maintains information about the application's status and oversees the allocation of resources in collaboration with the cluster manager.

**Spark Application** - designed to perform a specific data processing task.

**Spark Jobs**: The driver breaks a Spark application into one or more jobs, each represented as a Directed Acyclic Graph (DAG), Spark's execution plan.

**Spark Stages**: DAG nodes are divided into stages based on operations that can be executed serially or in parallel. Stages often align with data transfer boundaries among executors.

**Spark Tasks**: Stages consist of tasks, the smallest execution unit, each working on a single data partition. Tasks are distributed across executors, enabling parallel processing.

