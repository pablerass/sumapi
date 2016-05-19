#!/bin/bash

FILES="Dockerfile Dockerrun.aws.json requirements.txt sumapi.py"
ZIP_NAME="sumapi.zip"

for FILE in $FILES; do
	zip -ur $ZIP_NAME $FILE
done