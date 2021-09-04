- Kubeflow is a tool for orchestrating complicated workflows running on Kubernetes
- Every step of a Kubeflow pipeline is a seperate container
- The reason Kubeflow is the front runner in the MLOPs space is because it

## Kubeflow Pipeline
- Kubeflow pipeline is a description of ML workflow with all its components
- A component can be responsibel for different steps in the ML process - data processing, transformation, model training, validation
- KFP enables you to describe a workflow with individual steps - where each step is a container microservice or serverless function, through a python SDK
	- Executre that workflow on the cluster
	- & track the progress and experiment results