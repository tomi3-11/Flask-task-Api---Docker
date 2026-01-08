#!/bin/bash

for task in \
	'{"title": "Task A", "description": "Desc A"}' \
	'{"title": "Task B", "description": "Desc B"}' \
	'{"title": "Task C", "description": "Desc C"}'
do 
	curl -X POST http://localhost:5000/create \
	     -H "Content-Type: application/json" \
	     -d "$task"
done
