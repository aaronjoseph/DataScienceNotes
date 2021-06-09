Hadoop is an opensource software for reliable, scaleable, distributed computing. This works on distributed computing. 

Hadoop is designed with the fundamental assumptions of
- Hardware faliures are common
- And such faliures should be handled by the framework

Hadoop consists of
- Storage Part [[HDFS]] also known as Hadoop Distributed File System 
- Framework to process data across multiple servers - [[MapReduce]] 
- [[YARN]] - Yet Another Resource Negotiator is the architecture for distribution cluster, which runs and manages the data processing task
  
   ## Cordination between Hadoop Blocks
   
   1. User Defines map and reduce tasks using the MapReduce API
   2. `MapReduce` Then triggers the task, which is taken by `YARN`
   3. `YARN` figures out where and how to run the job and stores the results in `HDFS`

