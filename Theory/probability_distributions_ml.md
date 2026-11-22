# Probability Distributions in Machine Learning

## Introduction

Probability distributions describe how values of a random variable
are distributed.

They are important in statistical modeling, machine learning,
and uncertainty estimation.

## Common Probability Distributions

### 1. Normal Distribution

A continuous distribution with a bell-shaped curve.

Applications:
- Measurement errors
- Statistical modeling
- Gaussian Naive Bayes

### 2. Bernoulli Distribution

Represents a random variable with two possible outcomes.

Example:
- Success or failure
- Yes or no

### 3. Binomial Distribution

Models the number of successes in a fixed number of independent
Bernoulli trials.

### 4. Poisson Distribution

Models the number of events occurring within a fixed interval.

Examples:
- Customer arrivals
- Call frequency
- Event counts

### 5. Uniform Distribution

Every value within a specified interval has equal probability density
for a continuous uniform distribution.

## Python Example

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

normal = np.random.normal(0, 1, 1000)
uniform = np.random.uniform(0, 1, 1000)
poisson = np.random.poisson(5, 1000)

plt.hist(normal, bins=30, alpha=0.5, label="Normal")
plt.hist(uniform, bins=30, alpha=0.5, label="Uniform")

plt.title("Probability Distributions")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.legend()

plt.show()

print("Poisson Sample Mean:", np.mean(poisson))
```

## Applications

- Bayesian learning
- Statistical inference
- Generative modeling
- Anomaly detection
- Risk estimation

## Conclusion

Probability distributions provide the mathematical foundation
for understanding uncertainty and modeling random variables.
