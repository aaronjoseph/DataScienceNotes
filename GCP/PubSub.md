- It is a messaging middleware
	- It is a real time service
- It is a many to many asynchronous messaging
- **Pub/Sub** stands for Publisher & Subscriber 
- **Publisher** apps create and send messages on a Topic
- **Subscriber** apps subscribe to a topic to receive messages
- Subscription is queue to a subscriber

Major qualities of PUB/SUB
- Availability
- Durability
- Scalability


## Latency Issues

Pub/Sub has latency issues, and this can cause the messages to delivered in any order. Since Pub/Sub is a global service and the data traverses a mesh network, some messages will take more time than the other.