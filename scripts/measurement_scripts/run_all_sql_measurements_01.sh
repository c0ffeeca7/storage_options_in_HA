#!/bin/bash

path_to_scripts="yourPath"
#path_to_tests="${path_to_scripts}/sqlite3db/states_groupby_day.sql"
path_to_tests="${path_to_scripts}/sqlite3db/*.sql"

for f in $path_to_tests
do
    for i in {1..50}
    do
    	echo "Running iteration ${i}"
        ${path_to_scripts}/run_sql_measurement.sh ${path_to_scripts}/sqlite3db/pythonsqlite.db $f
    done
done
