```mermaid
 flowchart LR 
 A[Scoping] -->B[Data] --> C[Modeling] --> D[Deployment]
 ```

Under Deployment we have the following
- Downtime
- Runtime & Logical Error
- Distribution Faliure
- Data Faliure
- Service Faliure 

Deployment is the last stage of MLOPs. Herein, model's are pushed to production

### Key Challenges of Deployment

Key challenges in MLOPs are of two kinds `Software Related` & `Statistical Related`

**Statistical Related** - `Related to sudden shifts in data distributions`
1.  [[Concept Drift]]
2.  [[Data Drift]]

**Software Engineering **

> Checklist of questions
1. Realtime or Batch
2. Cloud or Edge/Browser
3. Computer Resources (CPU/GPU/Memory)
4. Latency, throughput (QPS)
5. Logging
6. Security and Privacy

### Deployment Type

1. New Product/Capability
2. Automate/assit with manual task
3. Replace previous ML system


### Deployment Pattern

1. [[Canary Deployment]]
2. [[Blue Green Deployment]]
3. [[Shadow Deployment]]

### Spectrum of Automation

```mermaid
flowchart LR 
A[Human Only] -->B[Shadow Mode]
B --> C[AI Assistance]
C --> D[Partial Automation]
D --> E[Full Automation]
```