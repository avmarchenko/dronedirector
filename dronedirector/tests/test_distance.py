# -*- coding: utf-8 -*-
# Copyright 2018 Alex Marchenko
# Distributed under the terms of the Apache License 2.0
"""
Tests for Distance Utilities
#################################
"""
import pytest as pt
import numpy as np
from dronedirector.distance import (equatorial_radius, polar_radius,
                                    earth_radius, lon_to_rad, lat_to_rad)


def test_lat_to_rad():
    """Test for :func:`~dronedirector.distance.lat_to_rad`."""
    assert np.isclose(lat_to_rad(90.0), 1.5707963268)
    assert np.isclose(lat_to_rad(0.0), 0.0)
    assert np.isclose(lat_to_rad(-90.0), -1.5707963268)
    with pt.raises(ValueError):
        lat_to_rad(180)
        lat_to_rad(-180)


def test_lon_to_rad():
    """Test for :func:`~dronedirector.distance.lon_to_rad`."""
    assert np.isclose(lon_to_rad(180.0), np.pi)
    assert np.isclose(lat_to_rad(90.0), 1.5707963268)
    assert np.isclose(lon_to_rad(0.0), 0.0)
    assert np.isclose(lat_to_rad(-90.0), -1.5707963268)
    assert np.isclose(lon_to_rad(-180.0), -np.pi)
    with pt.raises(ValueError):
        lon_to_rad(360)
        lon_to_rad(-360)


def test_earth_radius():
    """Test for :func:`~dronedirector.distance.earth_radius`."""
    assert np.isclose(earth_radius(1.570796326), polar_radius)
    assert np.isclose(earth_radius(0.0), equatorial_radius)
    assert np.isclose(earth_radius(-1.570796326), polar_radius)
