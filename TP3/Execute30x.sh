#! /bin/bash

for((count=0; count<30; count++))
do
python classification.py "$count"
done