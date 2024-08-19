#!/bin/bash

echo "Configurando el entorno"
pipx install poetry
poetry init -n
pip install typing-extensions
poetry env use python3.12
poetry add git+https://github.com/algorandfoundation/algokit-utils-py
poetry shell




