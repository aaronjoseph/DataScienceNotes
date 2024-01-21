- Study of machine learning explainability involves understanding the predictions made by the machine learning model
- When a model makes prediction, such predictions cannot be acted upon on blind faith, since the consequences may be catastrophic


```mermaid
graph TB
    subgraph "Programming"
    A[Input] --> B[Algorithm]
    B --> C[Output]
    end


```
```mermaid
graph TB

    subgraph "Machine Learning"
    D[Data] --> E[Algorithm]
    E --> F[Model]
    F --> G[Output]
    H[Labels] -.-> E
    end

    subgraph "Training"
	H -.-> K
	D --> K
	K --> E
    end

    subgraph "Inference (Testing)"
    D --> A
    A --> F
    end

```


