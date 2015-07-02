VecPy: Some Linear Algebra Basics in Python
===========================================

.. image:: https://img.shields.io/pypi/v/requests.svg
    :target: https://pypi.python.org/pypi/vecpy

.. image:: https://img.shields.io/pypi/dm/requests.svg
        :target: https://pypi.python.org/pypi/vecpy

A quick one:

.. code-block:: python

    >>> from vecpy import Vector as Vec
    >>> v = Vec(0, 2)
    >>> w = Vec([1, 3])
    >>> v + 2 
    >>> v + w 

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

This is a simple package allowing to complete very basic linear algebra tasks.

It is best explained by example:

.. code-block:: python

    >>> v = Vec(0, 2)
    >>> w = Vec(1, 3)


You can do basic rescaling of a vector:

.. code-block:: python

    >>> v_twice = v ^ 2
    >>> print v_twice.length == 2 * v.length
    >>> v_unit = v ^ 0
    >>> print v_unit.length
    
Adding scalar and other vectors:

.. code-block:: python
    >>> v + 2
    >>> v + w
    ...


Multiplication and dot-product

.. code-block:: python

    >>> v * 3
    >>> v.dot(w)

A vector has several properties:

.. code-block:: python

    >>> v.length
    >>> v.dim
    
You can specify which norm to use (default is the Euclidean)

.. code-block:: python

    >>> v.norm(1)
    >>> v.norm('inf')
    >>> v.norm(2) == v.length
    ...
        
You can project one vector on another:

.. code-block:: python

    >>> w_proj_v = v.proj(w)
    >>> ratio = v.proj(w, get_scale=True)

Iteration is supported as well:

.. code-block:: python

    >>> print [xi for xi in v]

String representations:

.. code-block:: python

    >>> print str(v)
    >>> print '{:[x, y, z]'.format(v)
