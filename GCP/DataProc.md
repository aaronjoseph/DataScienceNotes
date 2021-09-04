- Manged Hadoop + Spark
	- This gives you all the power of Hadoop without having to manage clusters
	- You can lift and shift your existing Hadoop & Spark workloads
	- Connect with cloud storage to seperate compute and storage
	- Re-seize clusters effortlessly. Preemptible VMs for cost savings
- Includes Hadoop, Spark, Hive & Pig
- `No-Ops` Create cluster, use it and turn it off
	- Uses Google Cloud Storage, not HDFS - else billing will be hurt
	
### Pre-emptiable Instances
- Pre-emptiable instance can also be used in DataProc
	- This is a VM instance, and can be utilised to keep costs down
		- This VM can be as cheap as 80% of a VM
		- However, the task should be fault-tolerant, since this instance can be taken up for other requirements

### Storing Data Off Cluster

- In DataProc, it is better to store data off-cluster
- This is because, in GCP memory on Compute instance is more expensive than other alternatives
	- Also, by doing this, the VM's can be switched off when not in use