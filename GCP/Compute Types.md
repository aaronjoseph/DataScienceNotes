There are 3 Major Compute system in GCP
- [[G Compute Engine (GCE)]]
- [[G Container Engine]]
- [[G App Engine]]

|              | App Engine | Container Engine        | Compute Engine                                      |
| ------------ | ---------- | ----------------------- | --------------------------------------------------- |
| Service Type | PaaS       | B/w PaaS & IaaS         | IaaS                                                |
| Description  | A flexible, zero ops (serverless) platform for building highly available apps | Logical infrastructure powered by Kubernetes | Virtual Machine running in Google's Data Centre Networks |
| Use Case     | You want to focus on writing code and never want to touch a server, cluster or Infra | You want to increase velocity and improve operability dramatically by separating the app from the OS | You need complete control over your infra and direct access to high performance hardware such as GPUs and local SSDs |
| OS Management | You neither know nor care about the OS running your code | You don't have dependencies on a specific operating system | You need to make OS level changes, such as providing your own network or graphic drivers, to squeeze out the last drop of performance |
| Workloads    | Websites; Mobile app and gaming backends | Containerized workloads | Any workload requiring a specific OS/OS config |
| Deployment   | Restful API | Cloud-native distributed systems | Currently deployed, on-prem software that you want to run in the cloud |
| Limitations  | IoT Apps | Hybrid Apps | Can't be containerized easily; or need existing VM images |
