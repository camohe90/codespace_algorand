#!/bin/bash

echo "running"
pipx install poetry
pip install typing-extensions
poetry init -n
pip install algokit-utils
#poetry add git+https://github.com/algorandfoundation/algokit-utils-py#feat/algorand_client




