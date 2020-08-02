### Task list

- [ ] How to get data from RDS to Sagemaker 
- [ ] Steps to call the sagemaker container
- [ ] How to do Batch Transform and push it to S3
- [ ] Find ways to use the existing container in S3 to deploy on AWS Quicksight
- [x] Find the steps for instance type
- [x] Spot instances
---

No need to think about the infrastructure since the entire service is managed

# Steps in a ML Workflow
1. Prepare the Data
2. Build a Model - Select the Model
3. Train and Tune the Model
	1. Set up and manage environments for training
	2. Train, debug and tune models
	3. Manage Training Runs
4. Deploy & Manage
	1. Deploy Model in production
	2. Monitor Models
	3. Validate Predictions
	4. Scale and manage production environment

Sagemaker is meant to envelop all the steps that is mentioned above
Sagemaker is a Web based IDE

# Data Annotation
`Sagemaker Ground Truth` - Where 3rd Party, public service or ML Automated Labeling services can be leveraged to automate the labeling of the data.

Ex : Sentiment Analysis, Labeling Image Data by Segement

`Sagemaker Processing` - Batch jobs, Feature Engineering, Data Cleaning. Fully Managed way and Fully Managed Services

- No need to provision or manage instances
- You can share the notebooks

`Sagemaker Autopilot` - Low Code implementation, inspects the data, build the candidate pipelines, tuninig model with high accuracy

AWS Market Place - Deploy on Sagemaker with minimal coding - quicker implementation

`Built-in-Algo` - Docker codes, configure the location and parameters
`Training Code` - Containers for Tensorflow and Sklearn,...
`Build your Own` - Your own container

Infrastructure is fully managed, training infra is on-demand. Spot instance - 60-70% on training cost

# Deployment
`HTTPS Endpoint` Is a realtime endpoint, 1 line of code 
`Batch Transform` 1 Line of code
`Amazon Container Services - ECS, EKS, Fargate`
`Run on S3`

# Sagemaker Model Monitor
- Collects data on the model
- Keeps an eye on the data



