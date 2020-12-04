export PYTHONPATH="${PYTHONPATH}:$(pwd)/"
export PYTHONPATH="${PYTHONPATH}:$(pwd)/backend/"
export PYTHONPATH="${PYTHONPATH}:$(pwd)/frontend/"

coverage run --source='.' -m unittest discover -s tests/ -p '*tests*.py'
coverage html
coverage report
