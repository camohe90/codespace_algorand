#!/bin/bash

echo "Running setup script..."

# Install Poetry using pipx
pipx install poetry

# Initialize a Poetry project without any interactive prompts
poetry init -n

# Add dependencies to the project
poetry add typing-extensions
poetry add fast-html htmx uvicorn

# Clone and install the Algokit Utils package
git clone https://github.com/algorandfoundation/algokit-utils-py.git
cd algokit-utils-py
pip install .
cd ..

echo "Setup completed."
