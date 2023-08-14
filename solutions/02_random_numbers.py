# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Exercises: Random Numbers

# %%
import numpy as np

# %% [markdown]
# ## 1. Create a Pseudo-Random Number Generator (PRNG) instance
#
# Create a PRNG and name it `rng`. Don't use a seed. Create several random numbers with `rng.random()`.
# Then, create a new, seedless `rng` and create several new random numbers. Note that these are different from before.

# %%
rng = np.random.default_rng()

# %%
rng.random()

# %%
rng.random()

# %%
rng.random()

# %%
rng = np.random.default_rng()

# %%
rng.random()

# %%
rng.random()

# %%
rng.random()

# %% [markdown]
# ## 2. Work with seeds
#
# Create a PRNG and seed it with a fixed number. Create a vector of 5 random normal-distributed numbers.
# Then, create a new PRNG with the same seed, and create a new vector of 5 random normal-distributed numbers. Observe that the numbers are identical to before.
#
# Finally, create a PRNG with a different seed and use it to create a new vector of 5 random normal-distributed numbers.

# %%
rng = np.random.default_rng(seed=2023)

# %%
rng.normal(size=5)

# %%
rng = np.random.default_rng(seed=2023)

# %%
rng.normal(size=5)

# %%
rng = np.random.default_rng(seed=2024)

# %%
rng.normal(size=5)

# %% [markdown]
# ## 3. Sample from a list of numbers
#
# Create an array named `squares` that contains the square numbers _0², 1², 2², ..., 9²_.
# Use a PRNG (`rng.choice()`) to sample 20 numbers from `squares`.

# %%
squares = np.arange(10)**2

# %%
rng = np.random.default_rng(seed=2023)

# %%
rng.choice(squares, size=20, replace=True)

# %%
