- REST stands for Representational State Transfer
- Protocol Independent
	- HTTP is the most common
	- Others possible like gRPC
- Service endpoints supporting REST are called RESTful
- Client and Server communicate with Request-Response processing
- URIs identify resources
	- Responses return an immutable representation of the resource information
- REST applications provide consistent, uniform interfaces
	- Representation can have links to additional resources
- Caching of immutable representation is appropriate

## REST-API

Characterstics of REST API
1. Simple and standardized
2. It can scale well and is stateless
3. It is highly performant and supports caching

REST API can be implemented using [[Microservices]]

## CRUD & REST Equivalent HTTP Method

Create   -> Post
Read      -> Get
Update  -> Put
Delete   -> Delete 

## HTTP Request Elements

- Verb : GET, PUT, POST, DELETE
- URI : Uniform Resource Identifier (endpoint)
- Request Header : Metadata about the message
	- Preferred representation formats (JSON, XML)
- Request Body : (Optional) Request state
	- Representation (JSON, XML) of resource

## HTTP Return Responses

- Response Code : 3-Digit HTTP status code
	- 200 codes for success
	- 400 codes for client errors
	- 500 codes for server errors
- Response Body : contains resource representation
	- JSON, XML, HTML