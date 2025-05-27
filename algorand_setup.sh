#!/bin/bash

echo "Configurando el entorno"
pip install typing-extensions
pip install python-dotenv
python -m venv venv/
source venv/bin/activate  
pip install "algokit-utils"




