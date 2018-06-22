# -*- coding: utf-8 -*-
# Copyright 2018 Alex Marchenko
# Distributed under the terms of the Apache License 2.0
"""
Tests for Distance Utilities
#################################
"""
import numpy as np
from dronedirector.distance import (equatorial_radius, polar_radius, degree_to_rad,
                                    earth_radius)


def test_earth_radius():
    """Test for :func:`~dronedirector.distance.earth_radius`."""
    assert np.isclose(earth_radius(90.0), polar_radius)
    assert np.isclose(earth_radius(0.0), equatorial_radius)
