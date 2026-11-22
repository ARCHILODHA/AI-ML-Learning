# Bayesian Inference in Machine Learning

## Introduction

Bayesian inference is a statistical method that updates beliefs
about unknown parameters using observed data.

It is based on Bayes' theorem.

## Bayes' Theorem

```text
P(A|B) = [P(B|A) × P(A)] / P(B)
```

Where:

- P(A|B): Posterior probability
- P(B|A): Likelihood
- P(A): Prior probability
- P(B): Evidence

## Important Concepts

### Prior

The probability assigned to a hypothesis before observing new data.

### Likelihood

The probability of observing the available data under a hypothesis.

### Posterior

The updated probability after considering the evidence.

### Evidence

The overall probability of observing the data.

## Example

Suppose:

- Probability of a disease = 0.01
- Test sensitivity = 0.90
- False positive rate = 0.05

The probability of testing positive is:

```text
P(Positive) =
P(Positive|Disease) × P(Disease)
+
P(Positive|No Disease) × P(No Disease)

= (0.90 × 0.01) + (0.05 × 0.99)
= 0.0585
```

Posterior probability:

```text
P(Disease|Positive)
= (0.90 × 0.01) / 0.0585
≈ 0.1538
```

Therefore, the probability of disease after a positive result
is approximately 15.38%.

## Applications

- Spam detection
- Medical diagnosis
- Bayesian optimization
- Recommendation systems
- Probabilistic forecasting

## Advantages

- Incorporates prior knowledge.
- Updates beliefs with new evidence.
- Provides uncertainty estimates.
- Supports probabilistic reasoning.

## Conclusion

Bayesian inference provides a systematic framework for updating
probabilities when new information becomes available.
