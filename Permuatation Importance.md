`Permuation Importance` calculates what features have biggest impact on predictions?

- This is calculated after the model has been fitted
- The premise here is : If a single feature is randomly shuffled, leaving the target and all others in place, how will it affect the final prediction performance. Here two things can play out
	- Less accurate predictions - since the data no longer corresponds to anything observed in the real world
	- Terrible performance, This will happen due to breakage in the strong relationship, which the model has picked up during training