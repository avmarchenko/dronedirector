# -*- coding: utf-8 -*-
# Copyright 2018 Alex Marchenko
# Distributed under the terms of the Apache License 2.0
"""
Test Aerial Objects
#####################
"""
from dronedirector.aerial import AerialObject, Drone, SinusoidalDrone, Coordinates


def test_aerial_objects():
    """Test that we can make generic aerial objects."""
    tree = AerialObject(altitude=cycle([100.0]),
                        latitude=cycle([37.8716]),
                        longitude=cycle([-122.2727]))
    assert isinstance(tree.coordinates, Coordinates)

