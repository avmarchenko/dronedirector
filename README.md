# Drone Director
A simple Python package for simulating aerial drones. The package has an API
for generating both static and dynamic objects that have altitude, latitude,
and longitude attributes. Functions are available for calculating relative
distances between objects. If the Confluent Kafka client is present (with
a corresponding server running somewhere), this package provides an API
for producing messages about the drones.
