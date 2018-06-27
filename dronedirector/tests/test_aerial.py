# -*- coding: utf-8 -*-
# Copyright 2018 Alex Marchenko
# Distributed under the terms of the Apache License 2.0
"""
Test Aerial Objects
#####################
"""
from itertools import cycle
from dronedirector.aerial import AerialObject, Drone, SinusoidalDrone


class CaliRedwood(AerialObject):
    """Example of subclassing."""
    def __init__(self):
        super(CaliRedwood, self).__init__(altitude=cycle([100.0]),
                                          latitude=cycle([37.8716]),
                                          longitude=cycle([-122.2727]))

def test_subclassing_ao():
    """Test subclassing :class:`~dronedirector.aerial.AerialObject`."""
    tree = CaliRedwood()
