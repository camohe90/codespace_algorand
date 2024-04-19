#!/bin/bash

echo "ejecutando"
pipx install poetry
poetry env use python3.12
pip install typing-extensions
poetry init -n
poetry add git+https://github.com/algorandfoundation/algokit-utils-py#feat/algorand_client
poetry shell


