# -*- coding: utf-8 -*-
# Copyright 2018 Alex Marchenko
# Distributed under the terms of the Apache License 2.0
"""
Kafka Producer
#################
This module provides a simple interface for generating messages from
:class:`~dronedirector.aerial.Drone`s
about their location (altitude, latitude, longitude). An 
Avro schema is provided for :class:`~dronedirector.aerial.Drone` messages.
"""
try:
    import confluent_kafka as ck
except ImportError:
    raise ImportError("Confluent Kafka Python client not available")
try:
    from confluent_kafka import avro
except ImportError:
    raise ImportError("Please install Avro to use this module")
import time


# value schema
drone_schema_str = """{
    "namespace": "dronedirector.drones",
    "name": "drone",
    "type": "record",
    "fields": [
        {
            "name": "uuid",
            "type": "string"
        },
        {
            "name": "county",
            "type": "string"
        },
        {
            "name": "datetime",
            "type": {
                "type": "long",
                "logicalType": "timestamp-micros"
            }
        {
            "name": "alt",
            "type": "double"
        },
        {
            "name": "lat",
            "type": "double"
        },
        {
            "name": "lon",
            "type": "double"
        }
    ]
}"""


def fly_drones(bootstrap_servers, schema_registry_url, producer_dict_kwargs=None,
               topic_name="raw_drones", time_delay=0, *drones):
    """
    A simple example of sending structured messages from drones to a message broker.

    Args:
        bootstrap_servers (str): Comma separated string of Kafka servers
        schema_registry_url (str): Schema registry URL
        topic_name (str): Topic name to which drone messages will be sent
        value_schema_str (str): Avro schema string for messages

    Warning:
        Changing the schema may require a custom definition of
        :class:`~dronedirector.aerial.Drone`.
    """
    pdk = {'bootstrap.servers': bootstrap_servers,
           'schema.registry.url': schema_registry_url},
    if isinstance(producer_dict_kwargs, dict):
        pdk.update(producer_dict_kwargs)
    producer = AvroProducer({'bootstrap.servers': bootstrap_servers,
                             'schema.registry.url': schema_registry_url},
                             default_value_schema=avro.loads(value_schema_str))
    for drone in drones:
        producer.produce(topic=topic_name, value=drone.message())
        time.sleep(time_delay)

    producer.flush()


value_schema = avro.loads(value_schema_str)
key_schema = avro.loads(key_schema_str)
value = {"name": "Value"}
key = {"name": "Key"}

avroProducer = AvroProducer({
'bootstrap.servers': '10.0.0.13',
'schema.registry.url': 'http://10.0.0.13:8081'
}, default_key_schema=key_schema, default_value_schema=value_schema)

avroProducer.produce(topic='my_topic', value=value, key=key)
avroProducer.flush()
