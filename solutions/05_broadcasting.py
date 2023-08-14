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
# # Exercises: Broadcasting

# %%
import numpy as np

# %% [markdown]
# ## 1. Combine arrays and scalars
#
# Create a random $4 \times 2$ array named $A$. Calculate the following expressions:
#
# - $A + 1$
# - $3A$
# - $2A - 3$
#
# Make sure you understand the results.

# %%
rng = np.random.default_rng(seed=2023)
A = rng.poisson(3, size=(4, 2))
A

# %%
A + 1

# %%
3 * A

# %%
2 * A - 3

# %% [markdown]
# ## 2. Combine 2-D and 1-D arrays
#
# Create a random $3 \times 4$ array $A$, a random $3$ array $x$, and a random $4$ array $y$.
#
# Which of the following expressions are allowed? Why?
#
# - `A + x`
# - `A * y` (elementwise multiplication)
# - `A * x[:, np.newaxis]`
# - `A - y[:, np.newaxis]`

# %%
A = rng.poisson(3, size=(3, 4))
x = rng.poisson(3, size=3)
y = rng.poisson(3, size=4)

# %%
# A + x  # Not allowed because the last dimensions are not compatible (A: 4, x: 3)

# %%
A * y

# %%
A * x[:, np.newaxis]

# %%
# A - y[:, np.newaxis]  # Not allowed because second-to-last dimensions are not compatible - but y[np.newaxis, :] would be allowed

# %% [markdown]
# ## 3. Higher dimensions
#
# Create a random $5 \times 3 \times 3$ array. You can think of this as a vector of five $3 \times 3$ matrices.
#
# Calculate the dot product of each of these five matrices with the vector $[1 \, 2 \, 3]$.

# %%
A = rng.poisson(3, size=(5, 3, 3))
A

# %%
A @ np.array([1, 2, 3])

# %%
A[0] @ np.array([1, 2, 3])

# %%
