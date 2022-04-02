Microservices divides a large program into multiple smaller, independent services. In a monolith application, all features are stored in a single code base. In microservices, there are multiple codebases, and each service manages its own data.

> A good microservice design is loosely coupled

## Pros & Cons of Microservices

Pro's | Con's
--|--
Easier to develop and maintain | Increased complexity when communicating between services
Reduced risks when deploying new versions | Increased latency across service boundaries
Services scale independently to optimize use of infrastructure | Concern about securing inter-service traffic
Faster to innovate and add new features | Multipe deployments
Can use different languages and frameworks for different services | Need to ensure that you don't break clients as version change
Choose the runtime appropriate to each service | Must maintain backward compatibility when clients as the microservice evolves

## Stateful & Stateless services

> Stateful applications and processes, are those that can be returned to again and again. They are performed with teh context of previous transactions and the current transation may be affected by what happened during previous transactions.

Stateful services manage stored data over time
- Harder to scale
- Harder to upgrade
- Need to back up

> A stateless process or application can be understood in isolation. There is no stored knowledge of or reference to past transactions.

Stateless services get their data from the environment of other stateful services
- Easy to scale by adding instances
- Easy to migrate to new versions
- Easy to administer

## 12 Factors App

Best Practices | Factors
--|--
Codebase | Use version control. Each app to have seperate repo
Dependencies | Use package manager. Declare dependencies in your codebase
Config | Do not put secrets, connection string, endpoints in the source code. Store as environmental variables
Backing Services | Databases, caching, queues and other service are accessed via URLs
Build, Release, Run | Build creates a deployment package from the source code. Release combines the deployment with configuration in the runtime. Run executes the application
Processes | Apps run in one or more processes. Each instance of the app gets its data from a seperate database services
Port Binding | Apps are self-contained and expose a port and protocol internally. Apps are not injected into a seperate server like Apache
Concurrency | Because apps are self-contained and run in seperate process, they scale easily by adding instances
Disposability | App instances should scale quickly when needed
Dev/Prod parity | Containers like Docker makes it easier. Leverage infra as code to make env easy to create
Logs | Write log messages to standard output and aggregate all logs to a single source
Admin Processes | Admin tasks should be repeatable processes, not one-off manual tasks