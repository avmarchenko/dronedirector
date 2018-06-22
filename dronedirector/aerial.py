# -*- coding: utf-8 -*-
# Copyright 2018 Alex Marchenko
# Distributed under the terms of the Apache License 2.0
"""
Aerial Objects
#################
This module provides some simple classes that are used to simulate flying
drones and other objects. The

Tip:
    Altitudes are expected in meters, latitudes and longitudes are expected
    in degrees. By convention N and E are positive angles and S and W are
    negative angles.

See Also:
    `World Geodetic System`_
    
.. _ref: https://en.wikipedia.org/wiki/World_Geodetic_System
"""
from __future__ import absolute_import
from collections import namedtuple
from abc import ABC, abstractmethod


Coordinates = namedtuple("Coordinates", ("altitude", "latitude", "longitude"))
Cartesian = namedtuple("Cartesian", ("x", "y", "z"))


class AbstractAerialObject(ABC):
    """
    Abstract base class for aerial objects.

    Aerial objects can be static or dynamic but must define something
    about their location (latitude, longitude) and how tall they are/how
    high up they fly. An example of a static aerial object (like a tree
    or building) is given below. Functions should be generators and may
    yield floating point or integer values.

    .. code:: Python

        class CaliRedwood(AbstractAerialObject):
            # Example of a completely static object
            def alititude(self):
                yield 100.0

            def latitude(self):
                yield 37.8716

            def longitude(self):
                yield -122.2727

    An example of a flying object can be found below.
    """
    @abstractmethod
    def altitude(self):
        """Generator that yields the current altitude of the object."""
        pass

    @abstractmethod
    def latitude(self):
        """Generator that yields current latitude of the object."""
        pass

    @abstractmethod
    def longitude(self):
        """Generator that yields current longitude of the object."""
        pass

    @property
    def coordinates(self):
        """
        Get the current coordinates of the object.

        Returns:
            coords (:class:`~aerial.Coordinates`): Named tuple of altitude, latitude, longitude
        """
        return Coordinates(altitude=next(self.altitude),
                           latitude=next(self.latitude),
                           longitude=next(self.longitude))

    def __init__(self):
        super(AbstractAerialObject, self).__init__()


class Drone(Drone):
    """

    """
