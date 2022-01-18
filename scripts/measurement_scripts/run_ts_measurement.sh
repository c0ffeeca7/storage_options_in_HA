#!/bin/bash

# measures cpu time, memory high water mark, and IO read writes used/performed by timescale process while running a given flux query.
# accepts the path as a variable from the calling method, run_all_timescale_measurements.sh.
path_to_current_script="$1"

if [ ! -f "${path_to_current_script}" ]; then
  echo "Please provide test script as argument."
  exit 1
fi

# Checks if timescale script is in current working directory.
if [ ! -f writeToTimescale.py ]; then
  echo "timescale queries missing. Store in current directory."
  exit 1
  #end if
fi

# systemctl automatically starts postgres. kill all postgres processes to start from scratch.
sudo pkill postgres

# delete linux file system cache (page cache). 
# https://linuxhint.com/clear_cache_linux/
# on sh -c: https://askubuntu.com/questions/230476/how-to-solve-permission-denied-when-using-sudo-with-redirection-in-bash
sudo sh -c "echo 3 > /proc/sys/vm/drop_caches"

# Assuming timescale scripts is present in current working directory. 
# Starts timescale in background (hence ampersand).
# using "time" to measure time used for this entire process.
echo "Starting timescale database..."
sudo systemctl start postgresql@14-main.service

# allow time for the db to start up.
sleep 5

#connect as user postgres
mkfifo postgrescmdpipe
sudo -u postgres psql postgres < postgrescmdpipe > /dev/null &
# get the PID of the psql process that just started.
PSQL_PID=$!

#echo "Logged on to postgres. Opening pipe..."
# Open command fifo for writing and assign fd 4
exec 4> postgrescmdpipe
#echo "Opened pipe. Starting to send commands..."

# start the stopwatch
timestamp_start=$(date +%s%N)
echo $timestamp_start
# Let's talk to postgresql
# connect to the database
echo "\c tsenergydata" >&4
# run the query
echo "\i ${path_to_current_script}" >&4 

# end of file, 
exec 4>&-

# wait for query to finish
wait $PSQL_PID

# delete query pipe
rm postgrescmdpipe

# stop the stopwatch
timestamp_end=$(date +%s%N)
#echo $timestamp_end
# calculate duration of query
realtime=$((timestamp_end-timestamp_start))

#echo $((realtime / 1000000))

# retrieve total cpu time from systemctl show (in nanoseconds)
# https://www.commandlinux.com/man-page/man1/systemctl.1.html 

process_stats="$(systemctl show postgresql@14-main.service)"
cputime=$(echo "${process_stats}" | grep -e "^CPUUsageNSec" | cut -f 2 -d "=" )

#echo "${cputime}"

# get current time
current_time=$(date --iso-8601=seconds)

# Get peak memory usage from cgroups in Bytes (systemctl show only shows current memory, not hwm).
# https://unix.stackexchange.com/questions/555080/using-cgroup-to-limit-program-memory-as-its-running
vmhwm=$(cat /sys/fs/cgroup/memory/system.slice/system-postgresql.slice/postgresql@14-main.service/memory.max_usage_in_bytes)

#echo "${vmhwm}"

# Get amount of reads and writes in bytes.
# https://man7.org/linux/man-pages/man5/proc.5.html
#io_disk_reads=$(cat /proc/"${INFLUXDB_PID}"/io | grep -e "^read_bytes" | cut -f 2 -d ':' | tr -d '[:space:]')
#io_disk_writes=$(cat /proc/"${INFLUXDB_PID}"/io | grep -e "^write_bytes" | cut -f 2 -d ':' | tr -d '[:space:]')
io_disk_reads=0
io_disk_writes=0
# get the name of the sql script file
filename=$(basename "${path_to_current_script}")
extension="sql_log.csv"
logfile="${filename%.sql}"_"${extension}"

# write timestamp, script name, cpu time(centisec-tsnano), memory_HWM(kB-tsBytes), disk reads, writes(bytes),realtime(ns)
echo "${current_time}","$filename","$cputime","$vmhwm","$io_disk_reads","$io_disk_writes","$realtime" >> "${logfile}"

# end timescaledb process
echo "Query completed. Going to kill the db... at pid $(pidof postgres)"
sudo systemctl stop postgresql@14-main.service


