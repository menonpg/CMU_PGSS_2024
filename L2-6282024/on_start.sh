#!/bin/bash

# This script runs every time your Studio starts, from your home directory.

# List files under fast_load that need to load quickly on start (e.g. model checkpoints).
#
# ! fast_load
# <your file here>

# Add your startup commands below.
#
# Example: streamlit run my_app.py
# Example: gradio my_app.py

curl -fsSL https://ollama.com/install.sh | sh
ollama run llava-phi3     
