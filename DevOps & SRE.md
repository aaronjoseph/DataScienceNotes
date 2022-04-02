- `SRE` is the practice of balancing the velocity of development features with the risk of reliability.
- `DevOps` is a philosophy, not a development methodology or technology. DevOPs breaks down silos between development and operations team
- SRE is a practical way of implementing DEVOPs
- Developers focus on feature velocity and innovation; operators focus on reliability and consistency

## Mission of SRE
To protect, provide for, and progress software and systems with consistent focus on availability, latency, performance and capacity

## High SRE Maturity

- Well documented and user-centric SLOs
- Error budgets
- Blameless postmortem culture
- Low tolerance for toil

## Blameless Postmortem / Retrospective

- Deteails of the incident and its timeline
- The actions taken to mitigate or resolve the incident
- The incident's impact
- Its trigger and root cause or causes
- The follow-up action to prevent its recurrence

## Reliability (Formulae)

= Good Time / Total Time = Fraction of time the service is available and working

## Error Budget
Error budget are the tool SRE uses to balance service reliability with the pace of innovation. Error budget forms a control mechanism for diverting attention to stability as needed. It is the level of unreliability you are willing to tolerate

# Service Level Terminology

## SLO & SLI
Sets the target for an SLI over a period of time. SLO is the number or the goal you want to acheive for a given SLI for a given duration.

Defining SLO's
- Service Level Indicators (SLIs)
	- A quantifiable measure of the reliability of your service from your users' perspective.
	- Expressed as a ratio of good events to a valid events times 100%
	- Map to user expectations
	- `SLI should be measurable`
- SLO's should be tied to SLI's aggregated over time, and should be close to 99.9% (three nines)

### Tips for Determining SLO's
- Goal isn't to make the SLO's as high as possible; It's is to keep it low while making users happy
- The higher the SLO's, higher the cost in computer resources and operations effort
- Applications should not significantly outperform their SLO's, because users come to expect the level of reliability you usually give them

## SLA
An SLA is a promise about the health of your service to your customers. `More restrictive version of SLO`  

[[Requirement Phase - MLOPs]]
