#!/bin/sh
docker build -t watertank .

echo "to run container:"
echo "  docker run --rm -p 5000:5000 watertank"
