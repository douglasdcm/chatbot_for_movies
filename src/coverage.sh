coverage run --source='.' -m unittest discover -s tests/ -p '*tests*.py'
coverage html
coverage report
