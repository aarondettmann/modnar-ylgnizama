Rotate points with complex numbers in 2D
========================================

Simple demonstration of rotation about the origin in 2D using complex numbers.

.. image:: example.gif

**General idea**

* Consider point ``(x, y)``
* Encode it as a complex number ``p = x + i*y``
* Encode the rotation operation as complex number ``z = cos(a) + i*sin(a)`` where ``a`` is the angle
* Rotating point ``(x, y)`` yields new coordinates ``(x', y')``
* Coordinates of rotated points are given as:

    * ``x' = real(p*z(a))``
    * ``y' = imag(p*z(a))``

**Equivalence with 2D rotation matrix**

With complex numbers:

.. code::

    p*z = (x + i*y)*(cos(a) + i*sin(a))
        = x*cos(a) + i*y*cos(a) + i*x*sin(a) - y*sin(a)
        = x*cos(a) - y*sin(a) + i*(x*sin(a) - y*cos(a))
        = x' + i*y'

Same rotation in matrix formulation:

.. code::

    / x' \   | cos(a)  -sin(a) |   / x \
    |    | = |                 | * |   |
    \ y' /   | sin(a)   cos(a) |   \ y /

See also:

* https://en.wikipedia.org/wiki/Rotation_(mathematics)
* https://en.wikipedia.org/wiki/Rotation_matrix

Requirements
------------

See ``requirements.txt``
