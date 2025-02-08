Apache Spark's architecture is designed to optimise data processing through several key components:

1. **Directed Acyclic Graph (DAG):**
   - **Definition:** A DAG is a finite graph with directed edges and no cycles, representing a sequence of computations where each node signifies an operation, and edges denote data dependencies.
   - **Role in Spark:** When a Spark application is executed, Spark constructs a DAG to represent the series of transformations and actions specified in the code. This DAG outlines the logical execution plan, allowing Spark to identify opportunities for optimisation and parallel execution. 
2. **DAG Scheduler:**
   - **Function:** The DAG Scheduler interprets the logical DAG and divides it into stages based on transformations. Each stage comprises tasks that can be executed in parallel.
   - **Process:**
     - Identifies stages by analysing transformations and their dependencies.
     - Submits stages to the Task Scheduler for execution.
     - Handles task failures by retrying or resubmitting stages as necessary.
   - **Benefits:** This approach enables efficient task scheduling, fault tolerance, and resource management, enhancing overall performance. 
3. **Tungsten Execution Engine:**
   - **Overview:** Tungsten is Spark's physical execution engine, introduced to improve CPU and memory efficiency. It focuses on low-level optimizations to maximize hardware utilization.
   - **Whole-Stage Code Generation:**
     - **Concept:** Tungsten employs whole-stage code generation to compile multiple operations into a single optimised function, reducing the overhead of virtual function calls and leveraging CPU registers for intermediate data.
     - **Advantages:**
       - Minimizes CPU cycles by eliminating unnecessary function calls.
       - Enhances cache locality and reduces memory access latency.
       - Improves execution speed by generating efficient bytecode at runtime.
     - **Implementation:** During query execution, Spark generates Java bytecode that fuses multiple physical operators into a single function, streamlining the execution process. 
