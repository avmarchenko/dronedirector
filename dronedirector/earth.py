# -*- coding: utf-8 -*-
# Copyright 2018 Alex Marchenko
# Distributed under the terms of the Apache License 2.0
"""
Earth Functions
######################
This module provides functions for determining distances between aerial
objects (static and dynamic) which are near the surface of planet Earth.

Tip:
    Altitudes are expected in meters, latitudes and longitudes are expected
    in degrees. By convention N and E are positive angles and S and W are
    negative angles.

See Also:
    `World Geodetic System`_
    
.. _ref: https://en.wikipedia.org/wiki/World_Geodetic_System
"""
import numpy as np
import numba as nb
    
    # These should be global statics somehow...consenting adults
    a = 6378137.0   # Equatorial radius in m
    b = 6356752.3   # Polar radius in m
    a2b = a**2*b
    
    @nb.jit(nopython=True, nogil=True)   # maybe make a copy for vectorization
    def get_sea_level(latitude):
    """
    Compute the radius of the Earth.
    
    The Earth isn't exactly spherical; depending on what latitude
    an object is at, the distance from sea-level to the center of
    the Earth varies slightly.
    """
    return a2b/((a*np.cos(latitude))**2 + (b*np.sin(latitude))**2)
    
    def test_get_sea_level():
    assert np.isclose(get_sea_level(np.pi/4), a)
    assert np.isclose(get_sea_level(np.pi), b)
