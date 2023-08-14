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
# # Introduction to NumPy
#
# Geir Arne Hjelle, geirarne@gmail.com
#
# <https://github.com/gahjelle/numpy-introduction>

# %% [markdown]
# ## Agenda
#
# - The NumPy array
# - Generating random numbers with NumPy
# - Vectorized operations
# - Linear algebra
# - Broadcasting

# %%
import numpy as np

# %% [markdown]
# ## The NumPy Array

# %% [markdown]
# You can convert lists and other iterables to NumPy arrays with `np.array()`:

# %%
np.array([1, 2, 3])

# %% [markdown]
# All elements in a NumPy array must have the same datatype. `np.array()` will cast to a common datatype if possible:

# %%
np.array([1, 2.3, 4])

# %%
np.array([1, "a", True, 3.14])

# %% [markdown]
# Typically, you'll work with arrays of integers or floats.

# %% [markdown]
# NumPy arrays can have several dimensions:

# %%
np.array([[1, 2, 3], [4, 5, 6]])

# %%
np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# %% [markdown]
# A one-dimensional array often represents a vector and a two-dimensional array typically represents a matrix:

# %%
x = np.array([-1, 0, 2], dtype="float64")
A = np.array([[1, 0, 1], [0, 1, -1], [-1, 1, 0]])

# %%
x.ndim

# %%
A.ndim

# %%
x.shape

# %%
A.shape

# %% [markdown]
# There are functions that can create special arrays (<https://numpy.org/doc/stable/user/basics.creation.html>):

# %%
np.zeros((2, 3))

# %%
np.ones((3, 2))

# %%
np.arange(1, 2, 0.1)

# %%
np.linspace(1, 2, 11)

# %%
np.eye(3)

# %%
np.diag([1, 2, 3])

# %% [markdown]
# You can **index** NumPy arrays similarly to Python lists:

# %%
A[2]

# %%
A[0, 1]

# %% [markdown]
# Note that you can index into all dimensions by separating the indices by commas. Slices can also be used:

# %%
A[1:]

# %%
A[1:, :1]

# %%
A[:, 2]

# %%
A[:, 2:3]

# %% [markdown]
# You can create new dimensions by indexing with `np.newaxis` (or `None`):

# %%
x[:, np.newaxis]

# %%
x[np.newaxis, :]

# %% [markdown]
# You can change the shape of an array with `.reshape()`:

# %%
x.reshape((3, 1))

# %%
A.reshape(9)

# %%
A.reshape(-1)

# %% [markdown]
# Note that `-1` is a placeholder that can be used in one dimension to represent the "necessary number of elements".

# %% [markdown]
# ## Generating Random Numbers

# %% [markdown]
# NumPy has a powerful mechanism for generating random numbers (<https://numpy.org/doc/stable/reference/random/index.html> and <https://realpython.com/numpy-random-number-generator/>):

# %%
rng = np.random.default_rng(seed=0xba5e1)
rng

# %% [markdown]
# An instance of a (pseudo)-random number generator (PRNG) can generate random numbers from many different distributions:

# %%
rng.uniform(0, 10)

# %%
rng.uniform(0, 10, size=(3, 3))

# %%
rng.normal()

# %%
rng.normal(size=10)

# %%
rng.normal(10, 5, size=(2, 4))

# %% [markdown]
# ## Vectorized Operations

# %% [markdown]
# One of NumPy's absolute superpowers is that it supports **vectorized operations**:

# %%
x = np.arange(5)
y = np.array([-1, 0, 1, 0, -1])
A = rng.poisson(5, size=(3, 3))
A

# %% [markdown]
# Operations on NumPy arrays are typically performed elementwise:

# %%
x + y

# %%
x * y

# %%
np.exp(x)

# %%
np.cos(y)

# %%
1 / A

# %% [markdown]
# **Side-note:** Vectorized operations means that you usually **DON'T** need to run loops when working with NumPy. This is important, especially for performance:

# %%
numbers_list = list(range(1_000_000))
numbers_array = np.array(numbers_list)

# %%
# %%timeit
[x**2 for x in numbers_list]

# %%
# %%timeit
numbers_array**2

# %% [markdown]
# `%%timeit` is a special Jupyter/IPython command that allows you to do simple benchmarking of code cells.

# %% [markdown]
# Some operators work on the whole array:

# %%
x @ y

# %% [markdown]
# The `@` operator performs dot-products on vectors. It'll do matrix multiplication if applied on a matrix:

# %%
z = np.array([1, 0, -1])
A

# %%
A @ z

# %%
z @ A

# %%
A @ A

# %% [markdown]
# ## Linear Algebra

# %% [markdown]
# NumPy is a great tool for doing linear algebra. There are several dedicated functions in the `np.linalg` module:

# %%
np.linalg.det(A)

# %%
np.linalg.norm(A)

# %%
np.linalg.inv(A)

# %%
np.linalg.inv(A) @ A

# %%
A.T

# %% [markdown]
# In practice, you more often work with non-square matrices. The **pseudoinverse** is useful in these cases:

# %%
A = np.array([[1, 2], [3, 0], [0, 2]])
b = np.array([30, 15, 20])

# %% [markdown]
# This represents the matrix and vector
#
# $$
# A = \begin{bmatrix} 1 & 2 \\ 3 & 0 \\ 0 & 2 \end{bmatrix}, \
# b = \begin{pmatrix} 30 \\ 15 \\ 20 \end{pmatrix}
# $$
#
# Consider the equation $Ax = b$ which can be expressed as the following:
#
# $$
# \begin{align}
# u + 2 v &= 30 \\
# 3u &= 15 \\
# 2v &= 20
# \end{align}
# $$
#
# Note that $x = (5, 10)$ or $u = 5$, $v = 10$ would be the solution to the system represented by the last two rows of $A$ and $b$. This is not consistent with the first row, so there is no exact solution to the equation $Ax = b$.

# %%
np.linalg.pinv(A)

# %%
np.linalg.pinv(A) @ b

# %%
np.linalg.lstsq(A, b, rcond=None)

# %% [markdown]
# See <RP> for more information.

# %% [markdown]
# ## Broadcasting

# %% [markdown]
# Broadcasting is a cousin of vectorization and makes many operations in NumPy extra powerful.
#
# In short, in many cases, NumPy can adapt the shape of an array to make it consistent with another.

# %%
A = rng.poisson(5, size=(3, 3))
x = np.arange(2, 7, 2)
A, x

# %%
A + A

# %%
A + x

# %% [markdown]
# Even though `x` is one-dimensional, it's broadcast into two dimensions. The first element of `x` is added to every element in the first column of `A`. The second element of `x` is added to every element in the second column of `A` and so on.
#
# A common usecase for broadcasting is for applying operations with scalars:

# %%
3 * A

# %%
x - 2

# %%
A * x - 10 / x

# %% [markdown]
# In operations that require "compatible" arrays, broadcasting works by comparing shapes starting at the "last" dimension. If one array has **one** element in that dimension, it will be broadcast to match the other array.

# %%
B = np.ones((4, 3, 2), dtype="int8")

# %%
B + np.arange(4).reshape(4, 1, 1)

# %%
B + np.arange(8).reshape(4, 1, 2)

# %% [markdown]
# You can use `np.newaxis` to control the broadcasting:

# %%
A + x[:, np.newaxis]

# %%
A + x[np.newaxis, :]

# %%
