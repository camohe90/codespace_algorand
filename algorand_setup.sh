#!/bin/bash

echo "Configurando el entorno"
pipx install poetry
pip install typing-extensions
poetry init -n
poetry add git+https://github.com/algorandfoundation/algokit-utils-py
poetry env use python3.12
poetry shell




