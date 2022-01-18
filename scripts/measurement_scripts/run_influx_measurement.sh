#!/bin/bash

# measures cpu time, memory high water mark, and IO read writes used/performed by influxd process while running a given flux query.
# needs to be run in the same directory as influxd. 

# accepts the path as a variable from the calling method, run_all_influx_measurements.sh.
path_to_current_script="$1"

if [ ! -f "${path_to_current_script}" ]; then
  echo "Please provide test script as argument."
  exit 1
fi

# Checks if influxdb is in current working directory.
if [ ! -f influxd ]; then
  echo "influxd binary missing, please download and store in current directory."
  exit 1
  #end if
fi

# delete linux file system cache (page cache). 
# https://linuxhint.com/clear_cache_linux/
# on sh -c: https://askubuntu.com/questions/230476/how-to-solve-permission-denied-when-using-sudo-with-redirection-in-bash
sudo sh -c "echo 3 > /proc/sys/vm/drop_caches"

# Assuming influxd is present in current working directory. 
# Starts influxdb in background (hence ampersand).
# using "time" to measure time used for this entire process.
echo "Starting influx database"
time ./influxd > influxdb.log &

# allow time for the db to start up.
sleep 5

# get the influxd process id
INFLUXDB_PID=$(pidof influxd)
echo "${INFLUXDB_PID}"

# start the stopwatch
timestamp_start=$(date +%s%N)

# run the query in influxdb
./influx query --file "${path_to_current_script}" > /dev/null

# stop the stopwatch
timestamp_end=$(date +%s%N)
# calculate duration of query
realtime=$((timestamp_end-timestamp_start))


# retrieve kernel and user execution time, add them up to total cpu time.
# https://man7.org/linux/man-pages/man5/proc.5.html 
# according to 'getconf CLK_TCK' (clock tick), the unit is 1/100 of a second. so 616 means 6.16 seconds.
process_stats=$(cat /proc/"$(pidof influxd)"/stat)
utime=$(echo "${process_stats}" | cut -d ' ' -f 14)
stime=$(echo "${process_stats}" | cut -d ' ' -f 15)
cputime=$((utime+stime))
#echo ${cputime}

# get current time
current_time=$(date --iso-8601=seconds)

# Get peak memory usage (high water mark: VmHWM) in kB.
# https://ewx.livejournal.com/579283.html
mhwm=$(cat /proc/"${INFLUXDB_PID}"/status | grep -e "^VmHWM" | cut -f 2 -d ":" | tr -d '[:space:]')
vmhwm=${mhwm::-2}
#echo ${mhwm}
#echo ${vmhwm}

# Get amount of reads and writes in bytes.
# https://man7.org/linux/man-pages/man5/proc.5.html
io_disk_reads=$(cat /proc/"${INFLUXDB_PID}"/io | grep -e "^read_bytes" | cut -f 2 -d ':' | tr -d '[:space:]')
io_disk_writes=$(cat /proc/"${INFLUXDB_PID}"/io | grep -e "^write_bytes" | cut -f 2 -d ':' | tr -d '[:space:]')

# get the name of the flux script file
filename=$(basename "${path_to_current_script}")
extension="influx_log.csv"
logfile="${filename%.flux}"_"${extension}"

# write timestamp, script name, cpu time(centisec), memory_HWM(kB), disk reads, writes(bytes),realtime
echo "${current_time}","$filename","$cputime","$vmhwm","$io_disk_reads","$io_disk_writes","$realtime" >> "${logfile}"


# end influxdb process
echo "Query completed. Going to kill the db... at pid ${INFLUXDB_PID}"
kill "${INFLUXDB_PID}"


