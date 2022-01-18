#!/bin/bash

path_to_scripts="your-path-here"
#path_to_tests="${path_to_scripts}/states_groupby_day.sql"
path_to_tests="${path_to_scripts}/*.sql"

for f in $path_to_tests
do
    for i in {1..50}
    do
    	echo "Running iteration ${i}"
        ${path_to_scripts}/run_ts_measurement.sh $f
    done
done
