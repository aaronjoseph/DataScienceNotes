 It is an infrastructure for automating, monitoring and maintaining model training and deployment in an end-to-end manner.
 
 ML pipeline workflows are usually DAGs.
 
 ```mermaid
 flowchart LR 
 A[Scoping] -->B[Data] --> C[Modeling] --> D[Deployment]
 ```
 
 The [[Machine Learning Life Cycle - MLOPs | MLOPs lifecycle]] can be formulated and encapsulated into an ML Pipeline, overlapping onto all  aspects of pipeline. 
 
 TFX - Tensorflow Extended, can be used for deploying production ML pipelines.