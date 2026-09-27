---
note_type: concept
search_stage: serving
tags:
  - gcp
  - search-eng
---

## What IAM Answers

Identity and Access Management (IAM) controls **which principal can perform which action on which resource**. Authentication establishes an identity; authorization evaluates its access. A principal may be a person, group, service account, or federated workload identity. Roles package permissions; policy bindings grant roles on resources.[^iam]

## Types of Roles

| Type | Meaning | Practical choice |
|---|---|---|
| Basic | Broad roles such as Owner, Editor, Viewer | Avoid using them as a convenient production default |
| Predefined | Service-maintained permissions for a task | Start here when an appropriate role exists |
| Custom | A maintained set of selected permissions | Use when predefined roles cannot meet the scope |

A custom role is not automatically safer: missing permissions can break operations, and excessive ones still grant excessive access.

## Resource Hierarchy and Effective Access

Allow policies inherit through organization → folder → project → resource. A child's allow policy does not simply replace the parent's grants. Effective access can also depend on deny policies, conditions, and principal access boundaries. Sibling projects share inherited grants but can have different local policies.[^iam]

Organization Policy constrains resource configurations and behavior; it is not interchangeable with IAM permission grants. An Organization Policy Administrator is not automatically an unrestricted administrator of every service.

## A Repeatable Permission Workflow

1. Name the actual caller: deployment job, runtime service account, analyst, or end user.
2. Identify the failing operation and target resource.
3. Inspect direct and inherited permissions plus applicable restrictions.
4. Grant the narrowest suitable role at the appropriate resource scope.
5. Test both the required operation and an operation that should remain denied.
6. Review audit records and remove temporary grants after their purpose ends.

Example: a search API reads model artifacts from one bucket. Grant its runtime identity read access there; do not grant project-wide Editor merely because the deployer also needs to publish revisions. See [[Service Account]] and [[Cloud Build]].

## Common Failure Modes

- Testing with personal administrator credentials and assuming production uses the same identity.
- Granting a role in the wrong project or to the build account instead of the runtime account.
- Ignoring inherited access when trying to reduce privileges.
- Treating a network timeout as proof of an IAM problem; [[VPC]] reachability is a separate boundary.
- Expecting a permission change to propagate instantaneously.[^iam]

> [!tip]- Explain a permission without naming a broad role
> State the principal, operation, and resource first: “The indexer must create objects in the index bucket.” Then choose and verify a role that implements that requirement.

## Exercise

A deployment succeeds, but the running service cannot read its model. List which two identities you would inspect and which evidence would distinguish authorization failure from network failure.

## References & Useful Links

[^iam]: [IAM overview](https://docs.cloud.google.com/iam/docs/overview) — Principals, roles, inheritance, access restrictions, and propagation.
- [Resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) — Policy attachment points and organizational structure.
