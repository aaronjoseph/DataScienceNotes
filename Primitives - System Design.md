In system design interviews, **primitives** refer to fundamental components or building blocks used to construct complex systems. These are essential services or modules that provide specific functionalities, which can be combined and orchestrated to design scalable and efficient systems. Common primitives include:

• **Load Balancers:** Distribute incoming network traffic across multiple servers to ensure no single server becomes a bottleneck, enhancing system reliability and performance.

• **Gateways:** Serve as intermediaries that manage tasks such as rate limiting and authentication, ensuring that only authorised and appropriately throttled requests reach the backend services.

• **Servers:** Handle client requests and execute application logic. They can be scaled horizontally to accommodate increased load.

• **Databases:** Store and manage data. Choices between SQL and NoSQL databases depend on factors like data structure, scalability needs, and consistency requirements.

• **Caches:** Temporarily store frequently accessed data to reduce latency and decrease the load on databases.

• **Message Queues:** Facilitate asynchronous communication between different parts of a system, decoupling components and improving scalability.

• **Content Delivery Networks (CDNs):** Distribute content to servers closer to end-users, reducing latency and improving load times.

