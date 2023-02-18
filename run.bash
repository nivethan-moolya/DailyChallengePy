#!/bin/bash
#for f in February/*.py; do coverage run --source . "$f"; done
py.test -v -s
pytest --html=report.html