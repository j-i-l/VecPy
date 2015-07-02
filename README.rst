VecPy: Some Linear Algebra Basics in Python
===========================================

.. image:: https://img.shields.io/pypi/v/requests.svg
    :target: https://pypi.python.org/pypi/vecpy

.. image:: https://img.shields.io/pypi/dm/requests.svg
        :target: https://pypi.python.org/pypi/vecpy


.. code-block:: python

    >>> from vecpy import Vector as Vec
    >>> # define a vector:
    >>> v = Vec(0, 2)  # or Vec((0, 2)) or Vec([0, 2])
    >>> w = Vec(1, 3)
    >>> # adding scalars and vectors
    >>> v + 2  # adds 2 to every coord
    >>> v + w  # adds coordinate by coordinate
    ...

Features
--------

- Basic operations ( dot-product, projection, rescaling, etc.)


Installation
------------

To install VecPy, simply:

.. code-block:: bash

    $ pip install vecpy


Documentation
-------------

This is a symple package allowing to complete very basic linear algebra tasks.

It is best explained by example:

.. code-block:: python
    >>> # define a vector:
    >>> v = Vec(0, 2)  # or Vec((0, 2)) or Vec([0, 2])
    >>> w = Vec(1, 3)
...

You can do basic rescaling of a vector:

.. code-block:: python
    >>> # get a vector with twice the lengt (same direction)
    >>> v_twice = v ^ 2
    >>> 
    >>> # get the unit vector
    >>> v_unit = v ^ 0
...
        
Adding scalar and other vectors:

.. code-block:: python
    >>> v + 2  # adds 2 to every coord
    >>> v + w  # adds coordinate by coordinate
...

Multiplication and dot-product

.. code-block:: python
    >>> # multiply by scalar
    >>> v * 3  # or 3 * v
    >>> # dot product
    >>> v.dot(w)
    >>> 
...

A vector has several properties:

.. code-block:: python
    >>> # Norm:
    >>> v.norm  # the default is the Euclidean norm (p=2)
    >>> # Lenth:
    >>> v.length  # addmitted this is just v.norm(2)
    >>> # Dimension:
    >>> v.dim
...

You can project one vector on another:

.. code-block:: python
    >>> # project one vector onto another
    >>> w_proj_v = v.proj(w)
    >>> # get length ration of a vector and the projection of another vector onto it
    >>> ratio = v.proj(w, get_scale=True)
...

Iteration is supported as well:

.. code-block:: python
    >>> # iterate through coordinates
    >>> print [xi for xi in v]
...

String representations:

.. code-block:: python
    >>> # string representation
    >>> print str(v)
    >>> print '{:[x, y, z]'.format(v)
    >>> # get unit vector
    >>> v ^ 0

