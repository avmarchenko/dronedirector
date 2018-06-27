# -*- coding: utf-8 -*-
# Copyright 2018 Alex Marchenko
# Distributed under the terms of the Apache License 2.0
"""
Test Aerial Objects
#####################
"""
import six
import json
import uuid
import numpy as np
from itertools import cycle
from dronedirector.aerial import AerialObject, Drone, SinusoidalDrone


class CaliRedwood(AerialObject):
    """Example of subclassing."""
    def __init__(self):
        super(CaliRedwood, self).__init__(altitude=cycle([100.0]),
                                          latitude=cycle([37.8716]),
                                          longitude=cycle([-122.2727]))

def test_simple_aerial():
    """Test making a simple object on-the-fly."""
    tree = AerialObject(altitude=cycle([100.0]),
                        latitude=cycle([37.8716]),
                        longitude=cycle([-122.2727]))
    msg = tree.message()
    assert isinstance(msg, six.string_types)
    assert isinstance(json.loads(msg), dict)


def test_subclassing_ao():
    """Test subclassing :class:`~dronedirector.aerial.AerialObject`."""
    tree = CaliRedwood()
    msg = json.loads(tree.message())    # Tests for valid json
    assert isinstance(msg, dict)
    assert np.isclose(msg['altitude'], 100.0)


def test_drone():
    """Test basic drone creation."""
    uid = uuid.uuid4()
    drone = Drone(cycle([1000.0]), cycle([41.0]), region="New York", uid=uid,
                  longitude=cycle(np.sin(np.arange(0, 2*np.pi, np.pi/360))))
    assert drone.region == "New York"
    assert drone.uid == uid
    msg = json.loads(drone.message())
    assert len(msg) == 6

