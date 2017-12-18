#!/bin/sh

python3 run.py & 
ngrok http 5000 & 

wait
