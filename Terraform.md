It is used to define Infrastructure as a code, using declarative language. It was developed by HashiCorp and is written in Go, which creates binary file, called `terraform`. This is translated to series of API calls to cloud providers, in the most efficient way possible.

It is 
- Open Source
- Cloud Agnostic Provisioning Tool
	- Which supports immutable infra
	- Declarative Language
	- Masterless & Agentless architecture

> The order in which the code is placed doesn't matter in terraform, you can have variables 


### Terraform Shell Commands

```shell
terraform init     # Initialize Terraform
terraform plan     # Plan Terraform
terraform apply    # Apply the changes
terraform destroy  # Destroy the terrafrom 
terraform destroy --auto-approve # Autoapproves the destroy
terraform state list # Shows the state
terraform state show # Shows detailed output
terraform output # Displays all the outputs
terraform refresh # Refreshes all the states

terraform destroy -target instance # Destroys particular instance
terrafrom apply -target instance # Creates a specific resource
```

### Terraform Files

- .terraform folder
	- This is created at the time of executing .terraform init code
- terraform.tfstate
	- This is the file which tracks all the resources created and tracks it
	- Deleting this file, will cause terraform to break

### Terraform Output Display

```shell
output "Text To Display"{
value = variable
}
```

### Terraform Variable


```py
variable "some_variable"{
	description = "Text"
	default = "" # This will be the default value applied
	type = "" # Type of the inputjjjjjjkj
}

# This can be referred as below
var.some_variable

```

> Variables can also be stored in terraform.`tfvars` file