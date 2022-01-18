#!/bin/bash


path_to_scripts="yourPath"
#path_to_tests="${path_to_scripts}/influxdb_01/groupby_week.flux"
#path_to_tests="${path_to_scripts}/influxdb_01/sum_phases_using_pivot_01.flux"
path_to_tests="${path_to_scripts}/influxdb_01/*.flux"

for f in $path_to_tests
do
    for i in {1..50}
    do
    	echo "Running iteration ${i}"
        ${path_to_scripts}/run_influx_measurement.sh $f
    done
done
