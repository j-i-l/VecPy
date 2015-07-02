__author__ = 'Jonas I Liechti'
from vecpy import Vector as Vec

# define a vector:
v = Vec(0, 2)  # or Vec((0, 2)) or Vec([0, 2])
w = Vec(1, 3)

# get a vector with twice the lengt (same direction)
v_twice = v ^ 2

# get the unit vector
v_unit = v ^ 0
v_unit = v.unit

# adding scalars and vectors
v + 2  # adds 2 to every coord
v + w  # adds coordinate by coordinate

# multiply by scalar
v * 3  # or 3 * v

# dot product
v.dot(w)

# get a norm
v.norm('inf')  # the default is the Euclidean norm (p=2)

# get the length of a vector
v.length  # this is just v.norm(2)

# get the dimension
v.dim

# project one vector onto another
w_proj_v = v.proj(w)

# get length ration of a vector and the projectoin of another vector onto it
ratio = v.proj(w, get_scale=True)

# iterate through coordinates
print [xi for xi in v]

# string representation
print str(v)
print '{:[x, y, z]}'.format(v)
