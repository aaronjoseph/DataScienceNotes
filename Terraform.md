It is used to define Infrastructure as a code, using declarative language. It was developed by HashiCorp and is written in Go, which creates binary file, called `terraform`. This is translated to series of API calls to cloud providers, in the most efficient way possible.

It is 
- Open Source
- Cloud Agnostic Provisioning Tool
	- Which supports immutable infra
	- Declarative Language
	- Masterless & Agentless architecture

Code to Deploy Terraform

```shell
terraform init
terraform apply
```