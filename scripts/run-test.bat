::!bin/bash

:: run pytest in virtualenv
poetry run pytest

:: clean up
cd ..
rmdir /s/q __pycache__