```mermaid
 flowchart LR 
 A[Scoping] -->B[Data] --> C[Modeling] --> D[Deployment]
 ```

Under Data we have the following
- Data Collection
- Data Ingestion
- Data Formatting
- [[Feature Engineering]]
- Feature Extraction
- [[Feature Selection]]

### Data Centric Approach

Data always requires refinement if we were to have robust Machine Learning Pipeline.

With the `Data Centric Approach`, there is a focus on the data. 

Type | Structured Data | Unstructured Data
---|---|---
Small Data | Housing Prices data from 50 examples | Manufacturing img data - 100 examples
Big Data | Online shopping reco for 1 Mil user | Speech reco from 50 Mil samples

**Structured Data**
- May or may not have huge collection of unlabeled examples 
- Humans can label more data
- Data Augmentation more likely to help

**Unstructured Data**
- May be more difficult to obtain more data
- Human labeling may not be possible

### [[Data Labeling]]

### Keep track of Data Provenance and Lineage

**Data Provenance** : Is the process of identifying where the data came from
**Data Lineage** : Is the process of identifying the steps before the data is finally created

The above two terms are quite important when it comes to data governance and documentation of both will help us understand issues with the data.

### Meta Data

Meta-Data is useful for
- Error Analysis, spotting unexpected effects
- Keeping track of data provenance

### Distribution Skew

Are of 3 types

- Dataset Shift : Case of dataset mismatch between training and serve data
$$P_{train}(y, x) \neq P_{serve}(y,x)$$
- [[Data Drift]]
$$P_{train}(y, x) = P_{serve}(y,x)$$
$$P_{train}(x) \neq P_{serve}(x)$$
- [[Concept Drift]]
$$P_{train}(y, x) \neq P_{serve}(y,x)$$
$$P_{train}(x) = P_{serve}(x)$$

### Basic Design for Skew Detection

```mermaid
flowchart TD 
A[Training Data] --> B[Baseline Stats]; 
A --> C[Schema]
D[Serving Data] --> E[Stats]
B --> F[Validate Statistics]
C --> F
E --> F
F --> G[Detect Anomalies]
G --> H[Alert and Analyze]
```