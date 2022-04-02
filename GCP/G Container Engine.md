> It is a mix of IaaS & PaaS

## Google [[Kubernetes]] Engine

GKE is about clusters running containers - containers have code packaged up with all its dependencies. GKE allows you to run containerized applications on a cloud environment that Google manages for you. Containerization is a way to package code that's designed to be highly portable and to use resources very efficiently. 

## Basic Functioning

- Since the underlyings are dependent on containers
	- The data isn't stored, it is ephemeral
	- Hence, to ensure data is stored use `GCP PersistentDisk`

Load Balancing
- Network load balancing works out of the box with Container Engine
- For HTTP load balancing, need to integrate with Compute Engine Load Balancing

`Kubernetes` is used for GKE

## Kubernetes Structure
- Kubernetes clusters have a collection of nodes
- In GKE, nodes are compute engine VMs
- Services are deployed into pods. A Pod is the most basic unit of Kubernetes
- You need to pay for the VM