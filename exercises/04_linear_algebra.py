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
# # Exercises: Linear Algebra

# %%
import numpy as np

# %% [markdown]
# ## 1. Linear algebra operations
#
# Create the following matrix:
#
# $$
# A = \begin{bmatrix}
#    1 &  2 & -1 \\
#   -1 & -1 &  2 \\
#    3 &  0 & -1
# \end{bmatrix}
# $$
#
# Calculate the following:
#
# - The transpose of $A$
# - The determinant of $A$
# - The inverse of $A$
# - The square of $A$, i.e. $A$ multiplied by itself

# %%

# %% [markdown]
# ## 2. Least-square equations
#
# Find the least-square solution to the following system:
#
# $$
# \begin{bmatrix}
#    1 &  2 & -1 \\
#   -1 & -1 &  2 \\
#    3 &  0 & -1 \\
#    2 & -1 &  0 \\
#    0 &  1 & -2
# \end{bmatrix}
# \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}
# = \begin{bmatrix} 10 \\ 15 \\ 20 \\ 25 \\ 30 \end{bmatrix}
# $$

# %%
