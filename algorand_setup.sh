#!/bin/bash

echo "Configurando el entorno"
pipx install poetry
poetry init -n
poetry env use python3.12
pip install typing-extensions
poetry add git+https://github.com/algorandfoundation/algokit-utils-py
poetry shell




