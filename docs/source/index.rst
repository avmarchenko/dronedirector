.. Copright 2018 Alex Marchenko
.. Distributed under the terms of the Apache License 2.0

#############################
`DroneDirector`_
#############################
A simple package for simulating flying drones and other aerial
objects. 

.. code-block:: Python

    from uuid import uuid4
    from itertools import cycle
    import dronedirector as dd
    tree = dd.AerialObject(altitude=cycle([100.0]), latitude=cycle([37.9]),
                           longitude=cycle([-122.3]))
    drone = dd.Drone(altitude=cycle([1000.0]), latitude=cycle([41.0]),
                     region="New York", uid=uuid4(),
                     longitude=cycle(np.sin(np.arange(0, 2*np.pi, np.pi/360))))
    sinedrone = dd.SinusoidalDrone(1000.0, 41.0, "New York", uid=uuid4(), speed=0.01)
    tree.message()    # Return JSON formatted message of tree's current location
    drone.message()   # {"altitude": 1000.0, "latitude": 41.0, "longitude": 0.0, "uid": "...", "region": "New York", "dronetime": "19700101000000000000"}' 

.. toctree::
    :maxdepth: 1
    :caption: Getting Started

.. toctree::
    :maxdepth: 2
    :caption: API

    api.rst


##################
Info
##################
:download:`License <../../LICENSE>`

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _DroneDirector: https://github.com/avmarchenko/dronedirector
