#!/usr/bin/bash

uvicorn source/server:app --reload
source server_env/bin/activate
