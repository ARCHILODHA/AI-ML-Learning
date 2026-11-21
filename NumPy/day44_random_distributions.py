import numpy as np

np.random.seed(42)

# Normal distribution
normal_data = np.random.normal(
    loc=0,
    scale=1,
    size=10
)

# Uniform distribution
uniform_data = np.random.uniform(
    low=0,
    high=10,
    size=10
)

# Binomial distribution
binomial_data = np.random.binomial(
    n=10,
    p=0.5,
    size=10
)

# Poisson distribution
poisson_data = np.random.poisson(
    lam=3,
    size=10
)

print("Normal Distribution:")
print(normal_data)

print("\nUniform Distribution:")
print(uniform_data)

print("\nBinomial Distribution:")
print(binomial_data)

print("\nPoisson Distribution:")
print(poisson_data)
