#!/bin/bash
set -e
cd /home/ubuntu/ai-interview-assistant
sudo docker stop interview-app || true
sudo docker rm interview-app || true
sudo docker build -t interview-app .
sudo docker run -d --name interview-app -p 80:8501 interview-app
