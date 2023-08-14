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
# # Exercises: Vectorized Operations

# %%
import numpy as np

# %% [markdown]
# ## 1. Find values of a function
#
# Create an array `x` of length 201 with values from `-10` to `10`. Compute the following functions:
#
# - $f(x) = x^2$
# - $f(x) = \log x$ (What happens for invalid values of $x$?)
# - $f(x) = 1 + 2 \sin x$ 

# %%
x = np.linspace(-10, 10, 201)

# %%
x**2

# %%
np.log(x)

# %%
1 + 2 * np.sin(x)

# %% [markdown]
# ## 2. Compare vectorized and non-vectorized code
#
# Redo the previous exercise for one of the functions, but this time solve it using an explicit loop instead of vectorization.
#
# How do the two solutions compare in terms of **readability** and **performance**?

# %%
np.array([1 + 2 * np.sin(n) for n in x])

# %%
# %%timeit
1 + 2 * np.sin(x)

# %%
# %%timeit
np.array([1 + 2 * np.sin(n) for n in x])

# %%
