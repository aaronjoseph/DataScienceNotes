## Google Kubernetes Engine

GKE is about clusters running containers - containers have code packaged up with all its dependencies. GKE allows you to run containerized applications on a cloud environment that Google manages for you. Containerization is a way to package code that's designed to be highly portable and to use resources very efficiently. 

## Basic Functioning

- Since the underlyings are dependent on containers
	- The data isn't stored, it is ephemeral
	- Hence, to ensure data is stored use `GCP PersistentDisk`

Load Balancing
- Network load balancing works out of the box with Container Engine
- For HTTP load balancing, need to integrate with Compute Engine Load Balancing

`Kubernetes` is used for GKE

>Master Endpoint Runs Node Instances run Kubelets
Each Kubelets controls a pod
Pods contain individual Docker containers

Kubernetes is a way to orchestrate code in containers. 

`Node Pool` are subset of machines within a cluster that all have the same configuration. This is useful for customizing instance profiles in your cluster

`Container Builder` tool that executes your container image builds on GCP infra. 
Working
- Import source code from a variety of repositories or cloud storage spaces
- Execute a build to your specification
- Produce artifacts such as Docker containers or Java archives

`Container Registry` Private registry for Docker images

Can access container registry through secure HTTPS endpoints which lets you push, pull and manage images from any system, whether it's a compute engine or your own hardware. 

`Autoscaling`

Automatic rescaling of cluster takes place with **Cluster Autoscaler**