# -*- coding: utf-8 -*-
# Copyright 2018 Alex Marchenko
# Distributed under the terms of the Apache License 2.0
"""
Distance Calculation Utilities
################################
This module provides functions for determining distances between aerial
objects (static and dynamic) which are near the surface of planet Earth.
This module makes use of compilation to speed up mathematical operations.

Tip:
    Altitudes are expected in meters, latitudes and longitudes are expected
    in degrees. By convention N and E are positive angles and S and W are
    negative angles.

See Also:
    `World Geodetic System`_
    
.. _ref: https://en.wikipedia.org/wiki/World_Geodetic_System
"""
from __future__ import absolute_import, division
import numpy as np
import numba as nb


equatorial_radius = 6378137.0              # Equatorial radius in meters
polar_radius = 6356752.3                   # Polar radius in meters
a2b = equatorial_radius**2*polar_radius    # Factor used to quickly compute radius


@nb.jit(nopython=True, nogil=True)
def lat_to_rad(degree):
    """
    Convert latitude (in degrees) to radians.

    Args:
        degree (float): Angle in degrees (e.g. +41.0 == 41.0 N).

    Returns:
        rad (float): Angle in radians
    """
    deg = -np.mod(degree, 90.0) if degree < 0 else np.mod(degree, 90.0)
    return deg*np.pi/180


@nb.jit(nopython=True, nogil=True)
def lon_to_rad(degree):
    """
    Convert longitude (in degrees) to radians.

    Args:
        degree (float): Angle in degrees (e.g. -122.0 == 122.0 W).

    Returns:
        rad (float): Angle in radians
    """
    deg = -np.mod(degree, 180.0) if degree < 0 else np.mod(degree, 180.0)
    return deg*np.pi/180

    
@nb.jit(nopython=True, nogil=True)
def _earth_radius(lat):
    """
    Compute the radius of the Earth.
    
    The Earth isn't exactly spherical; depending on what latitude
    an object is at, the distance from sea-level to the center of
    the Earth varies slightly.

    Args:
        latitude (float): Latitude in radians

    Returns:
        radius (float): Approximate distance to sea level at the current latitude in meters
    """
    return a2b/((equatorial_radius*np.cos(lat))**2 + (polar_radius*np.sin(lat))**2)
    
    
@nb.jit(nopython=True, nogil=True)
def to_cartesian(alt, lat, lon):
    """
    Convert altitude, latitude, and longitude to spherical coordinates.

    Distances are computed relative to the center of the earth.
    
    Args:
        alt (float): Altitude (above sea-level) in meters
        lat (float): Latitude in radians
        lon (float): Longitude in radians

    Returns:
        tup (tuple): Tuple of x, y, z coordinates in meters
    """
    r = alt + earth_radius(lat)
    x = r*np.sin(lat)*np.cos(lon)
    y = r*np.sin(lat)*np.sin(lon)
    z = r*np.cos(lat)
    return x, y, z, r
