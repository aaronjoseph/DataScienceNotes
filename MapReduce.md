Google created MapReduce. Google's challenge was to figure out how to index the exploding volume of content on the web. This was stored in [[Google File System]]. MapReduce is a form of data processing or programming paradigm. It also takes care of parallelism inherent in a distributed system.

In MapReduce, it breaks down into the following steps
- `Map` - A step that can be performed in parallel, here the mapping takes place, that is each machine will start looking for the document and assign a key-value pair to the mapper
- `Shuffle` - This is the intermediate step wherein, the value from the mapper is extracted and stored seperately in each of the machines  
- `Reduce` - This step will thereafter reduce the values in the shuffle stage, and save it
- `Result` -  The values from the reduce stage is finally collated in Result stage

[Paper](https://courses.cs.washington.edu/courses/cse547/17sp/content/Downloads/p107-dean.pdf)
