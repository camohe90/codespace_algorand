#!/bin/bash

echo "Configurando el entorno"
pip install typing-extensions
pipx install poetry
poetry init -n
poetry add git+https://github.com/algorandfoundation/algokit-utils-py
poetry shell




