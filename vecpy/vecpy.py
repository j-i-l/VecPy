# -*- coding: utf-8 -*-

"""
vecpy.vecpy
~~~~~~~~~~~
This module contains the Vector object.

"""
__author__ = 'Jonas I Liechti'


class Vector():
    def __init__(self, *args, **kwargs):
        if args:
            if len(args) == 1 and isinstance(args[0], (list, tuple)):
                _vec = args[0]
            elif len(args) == 2 and all([isinstance(arg, (list, tuple)) for arg in args]):
                # the vector is defined via two points (start and stop)
                # keep the two points
                _vec = (
                    args[1][0] - args[0][0],
                    args[1][1] - args[0][1],
                    args[1][2] - args[0][2] if len(args[0]) == 3 else 0.
                )
            else:
                _vec = args
            if len(_vec) == 2:
                _vec = list(_vec) + [0.]
            self.x, self.y, self.z = _vec
        else:
            self.x = kwargs.get('x', None)
            self.y = kwargs.get('y', None)
            self.z = kwargs.get('z', 0.0)
            if 'start_point' in kwargs:
                start_coords = kwargs.pop('start_point')
                end_coords = kwargs.pop('end_point')
                if len(start_coords) == 2:
                    self.z = 0.0
                else:
                    self.z = end_coords[2] - start_coords[2]
                self.x = end_coords[0] - start_coords[0]
                self.y = end_coords[1] - start_coords[1]
            # raise error if self.x/self.y are None

    @property
    def coords(self):
        return self.x, self.y, self.z

    @property
    def _coords(self):
        return self.x, self.y, self.z
    # to do: make coords take as many dims as input

    @property
    def length(self):
        return self.norm(2)

    @property
    def unit(self):
        return self ^ 0

    @property
    def dim(self):
        return len(self._coords)


    def __iter__(self):
        return self._coords.__iter__()

    # to do: implement getitem

    def dot(self, w):
        """ The dot product of self and other vector w.
        """
        return sum([xi_s * xi_w for xi_s, xi_w in zip(self, w)])

    def __add__(self, w):
        if isinstance(w, (int, float)):
            return Vector([xi + w for xi in self])
        else:
            return Vector([xi_s + xi_w for xi_s, xi_w in zip(self, w)])

    def __radd__(self, w):
        return self.__add__(w)

    def __sub__(self, w):
        return Vector([xi_s - xi_w for xi_s, xi_w in zip(self, w)])

    def __mul__(self, w):
        """ Returns the dot product of self and other if multiplied
            by another Vector.  If multiplied by an int or float,
            multiplies each component by other.
        """
        if isinstance(w, (float, int)):
            return Vector([w * _xi for _xi in self])
        else:
            return self.dot(w)

    def __rmul__(self, w):
        return self.__mul__(w)

    def __xor__(self, fct):
        """
        Returns a new rescaled Vector

        E.g.:
            - vec ^ 1 returns a new Vector object with the same coordinates as vec
            - vec ^ 0 returns the unit vector in the direction of vec as a new Vector object
            - vec ^ 2 returns a new Vector object that has twice the length of vec and points
                in the same direction

        :return:
        """
        if fct:
            _scale = fct
        else:
            _scale = 1 / self.length
        # to do: handle error
        return Vector([_xi * _scale for _xi in self])

    def __str__(self):
        return str([_xi for _xi in self])

    def __format__(self, to_format):
        if any([_xi in to_format for _xi in ['x', 'y', 'z']]):
            back_string = to_format.replace(
                'x', '{}'.format(self.x)
            ).replace(
                'y', '{}'.format(self.y)
            ).replace(
                'z', '{}'.format(self.z)
            )
        else:
            back_string = str(self)
        return back_string

    def norm(self, p=2):
        if p == 'inf':
            return max([abs(_xi) for _xi in self])
        else:
            return float(sum([abs(_xi) ** p for _xi in self]) ** (1 / float(p)))

    def proj(self, w, get_scale=False):
        """
        Project the Vector w onto the vector self
        Returns the projection of w onto self, i.e. another Vector
        if get_scale=True not a vector, but the rescaling factor is returned
        :param w:
        :return:
        """
        scale_fact = self.dot(w) / self.length ** 2
        if get_scale:
            return scale_fact
        else:
            return self ^ scale_fact

    def angle(self, w, degree=False):
        """
        Returns the angle (in radians by default)
        """
        from math import acos, pi
        cos_theta = self.dot(w) / (self.length * w.length)
        theta = acos(cos_theta)
        if not degree:
            return theta
        else:
            return theta / (2 * pi) * 360