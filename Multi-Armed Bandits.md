MAB is a form of [[AB Testing]] that uses machine leanring to learn from the data gathered during the test to dynamically increse the visitor allocation in favour of better performing variations. The core concept of MAB is `dynamic traffic allocation`. 

Unlike A/B tests, MAB maximizes the total number of conversions during the course of the test. The trade-off is that statistical certainty takes a backseat because the focus is on conversions and finding out the exact conversion rates.

## Eploration and Exploitation

There are two pillars to this algorithm
- Exploration
- Exploitation

The classic A/B testing is in perpetual `Exploration` state, discovering the exact conversion rate of variations.

In MAB, it adds exploitation in its arsenel, which makes it much better for the task.