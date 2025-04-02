#!/bin/sh

echo "Waiting for PostgreSQL..."
while ! nc -z db 5432; do
  sleep 1
done

echo "PostgreSQL is ready"

echo "Waiting for Mosquitto to be ready..."
while ! nc -z "$MQTT_BROKER" "$MQTT_PORT"; do
  sleep 1
done

echo "Mosquitto is up. Starting FastAPI..."
# Start the FastAPI server
exec "$@"
