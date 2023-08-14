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
# # Exercises: NumPy Arrays

# %%
import numpy as np

# %% [markdown]
# ## 1. Create a specific array
#
# Create an array representing the following matrix with NumPy:
#
# $$
# \begin{bmatrix}
#   1 &  4 & -2 &  1 \\
#   2 & -1 &  0 &  3 \\
#   0 &  0 &  1 &  9
# \end{bmatrix}
# $$

# %%
np.array([[1, 4, -2, 1], [2, -1, 0, 3], [0, 0, 1, 9]])

# %% [markdown]
# ## 2. Play with data types
#
# Create the same array as above, but make sure each element is a floating point number.

# %%
np.array([[1, 4, -2, 1], [2, -1, 0, 3], [0, 0, 1, 9]], dtype="float64")

# %%
np.array([[1.0, 4, -2, 1], [2, -1, 0, 3], [0, 0, 1, 9]])

# %% [markdown]
# ## 3. Prepare an array of a specific shape
#
# Create an array with all elements being `0` with the same shape as the array in exercise 1.

# %%
np.zeros((3, 4))

# %%
A = np.array([[1, 4, -2, 1], [2, -1, 0, 3], [0, 0, 1, 9]])
np.zeros_like(A)

# %% [markdown]
# ## 4. Create a constant array
#
# Create an array with 5 rows and 2 columns where all elements have the value `3.14`.

# %%
np.ones((5, 2)) * 3.14

# %%
np.full((5, 2), 3.14)

# %%
