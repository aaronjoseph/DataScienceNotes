Kubernetes is a way to orchestrate code in containers. 

Container orchestration engine
- Automating deployment, scaling and management of containerized applications
- Facilitates both declarative configuration and automation

## Kubernetes Components
- **Master** - Acts as the primary control plane for Kubernetes. Master are responsible at a minimum for running the API Server, scheduler and cluster controller. They commonly also manage storing cluster state, cloud-provider specific componets and other cluster essential services
- **Nodes** - Are the workers of a Kubernetes cluster. They run a minimal agent that manages the node itself and are tasked with executing workloads as designated by the master


>Master Endpoint Runs Node Instances run Kubelets
Each Kubelets controls a pod
Pods contain individual Docker containers -> `Smallest deployable unit in Kubernetes`


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

## Pods
Pods is a Kubernetes object. It is the logical application centric unit for hosting containers. Contains one or more tightly coupled containers. Designed around a single application or service.