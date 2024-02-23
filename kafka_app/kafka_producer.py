from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka import SerializingProducer

from config import config

# Producer will upload data to Confluent Kafka topic
def get_producer():
    schema_registry_client = SchemaRegistryClient(config["schema_registry"])
    youtube_videos_value_schema = schema_registry_client.get_latest_version("youtube_videos-value")

    serializer_config = {
        "key.serializer": StringSerializer(),
        "value.serializer": AvroSerializer(
            schema_registry_client, 
            youtube_videos_value_schema.schema.schema_str,
        ),
    }
    kafka_config = {**config["kafka"].copy(), **serializer_config} # join dict() using {**x, **y}

    producer = SerializingProducer(kafka_config)
    return producer

# Actions after producing (uploading) data
def on_delivery(err, record):
    if err:
        print(f"Error delivering message: {err}")
    else:
        print(f"Message delivered successfully:")
        print(f"  - Topic: {record.topic}")
        print(f"  - Key: {record.key}")












