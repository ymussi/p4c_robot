#!/bin/bash

cd /app/first-robot/robots

gunicorn app:app --bind 0.0.0.0:5000 -w 4 --reload --timeout 120

