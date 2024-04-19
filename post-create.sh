#!/bin/bash

echo "ejecutando"
pipx install poetry
pipx install --python python3.12 poetry
pip install typing-extensions
poetry init -n
poetry add git+https://github.com/algorandfoundation/algokit-utils-py#feat/algorand_client
poetry shell


