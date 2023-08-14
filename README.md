# Introduction to NumPy

This repository contains material for the tutorial I presented at the [EuroSciPy 2022](https://www.euroscipy.org/2022/) conference in Basel.

## Topics

The tutorial covers the following topics:

- The NumPy array
- Generating random numbers with NumPy
- Vectorized operations
- Linear algebra
- Broadcasting

## Description

NumPy is one of the foundational packages for doing data science with Python. It enables numerical computing by providing powerful N-dimensional arrays and a suite of numerical computing tools. In this tutorial, you'll be introduced to NumPy arrays and learn how to create and manipulate them. Then, you'll see some of the tools that NumPy provides, including random number generators and linear algebra routines.

This tutorial will be an introduction to numerical computing with Python and the NumPy library. It's intended for people who are new to NumPy and Python's scientific stack, or those who need a refresher. 

In this tutorial, you'll learn about different ways to create NumPy arrays. You'll see how you can pull out individual elements or sub-arrays from them. Even more importantly, you'll learn about broadcasting and vectorization. These are NumPy's superpowers that help you write code that's both readable and fast.

NumPy's arrays are the foundational building blocks. However, you'll also dip your toes into some of the numerical computing tools that are part of the library. In particular, you'll learn the best practices for working with random numbers in NumPy. Furthermore, you'll see how to perform linear algebra operations like matrix addition, multiplication, and inversion.

## Preparations

You should create a virtual environment and install numpy and other necessary dependencies.

> **Note:** Demonstrations were done on Linux Ubuntu with Python 3.11.4 and packages and versions specified in [`requirements.txt`](requirements.txt).

### Conda/Anaconda

If you have installed the full **Anaconda** distribution, you already have all the necessary dependencies on your system.

If you're running **Miniconda** or want to set up a separate environment for this tutorial, you can use `conda` to do so:

```console
$ conda env create -n euroscipy-numpy -f environment.yml
$ conda activate euroscipy-numpy
```

Remember to activate your Conda environment.

### Pip

If you're using a plain Python distribution, then you can use `venv` to create a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/):

```console
$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt
```

On Windows, you don't need `source` when activating your virtual environment. You can type `venv\Scripts\activate` instead.

## Exercises

You'll find the exercises in the [`exercises/`](exercises/) folder. You can open the `.py` files in your favorite editor. It may be helpful if your editor supports cells in script files. For example, [VS Code](https://code.visualstudio.com/) and [Spyder](https://www.spyder-ide.org/) support these cells and make it more convenient to run your solutions.

If you prefer to solve the exercises in Jupyter, you can convert the exercise files to notebooks using [`jupytext`](https://jupytext.readthedocs.io/):

```console
(venv) $ cd exercises/
(venv) $ jupytext --sync *.py
```

`jupytext` will convert all exercise files to notebooks that you can open in Jupyter Lab, or any other compatible notebook environment.

You can find solutions to all exercises in the [`solutions`](solutions/) folder.

## Demonstrations

The workshop mostly consists of live code demonstrations. You can find simple notes from the demos in the file [`numpy_introduction.py`](numpy_introduction.py). Use `jupytext` to convert the notes to a Jupyter Notebook if you prefer.

---

Demonstration code, exercises, and solutions are licensed under an [MIT license](LICENSE).
