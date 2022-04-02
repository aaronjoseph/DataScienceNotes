## Types of Roles

There are 3 types of roles in Cloud IAM
- Primitive Roles
	- Includes Owner, Editor and Viewer role
	- This was before cloud IAM came into the picture
- Predefined Roles
	- Gives granular roles for a specific service and are managed by GCP
- Custom Roles
	- Provides granular access according to a user-specified list of permissions


## Resource Hierarchy

The hierarcy is as follows
- Org Node
	- This is the root node for Google Cloud resources
	- Its the top of the hierarchy
	- Roles associated here
		- `Organization Policy Administrator` - Broad control over all cloud resources
		- `Project Creator` - Fine-grained control of project creation 
- Folders
	- There can be multiple folders within folders
- Projects
	- Folders can have mulitple projects under it
	- Folders group projects under an organization
	- Use folders to assign policies
	- All projects in a folder share the same IAM policies
- Resources
	- These are resources within individual project

## Service Account

- Provide an identity to carry out server-to-server interactions in a project

> Policy Inheritance - Is the principle by which policies at the top levels get inherited to the bottom. i.e -> From Org to Folder

## General Pointers
Grant roles to Google groups rather than individuals
- Groups can be more granular than job roles
- Use multiple groups for better control

**Roles**
- Prefer pre-defined roles over custom roles
- Grant roles at the smallest scope needed (PLP)
- Limit use of "owner" and "editor" roles
- Consider hierarchy inheritance when assigning roles