#!/bin/bash


# measures cpu time, memory high water mark, and IO read writes used/performed by SQLite process while running a given sql query.
#https://www.sqlite.org/c3ref/memory_highwater.html
# https://coderedirect.com/questions/515811/determining-execution-time-of-queries-in-sqlite


path_to_db="$1"

path_to_current_script="$2"

if [ ! -f "${path_to_current_script}" ]; then
  echo "Please provide test script as argument."
  exit 1
fi

# Check if sqlitedb is in current working directory.
if [ ! -f pythonsqlite.db ]; then
  echo "sqlitedb missing. Run this script in the directory containing the .db file."
  exit 1
  #end if
fi

# Check if another sqlite process is running already.
if pidof sqlite3; then
  echo "sqlite3 process already running. Kill process before running this script."
  exit 1
fi

# delete linux file system cache (page cache). 
# https://linuxhint.com/clear_cache_linux/
# on sh -c: https://askubuntu.com/questions/230476/how-to-solve-permission-denied-when-using-sudo-with-redirection-in-bash
sudo sh -c "echo 3 > /proc/sys/vm/drop_caches"

echo "Starting sqlite database and the script"

# Assuming sqlitedb is present in current working directory. 
# Create sqlite3 command fifo (named pipe)
# https://stackoverflow.com/questions/3462075/keep-a-file-open-forever-within-a-bash-script
mkfifo sqlite3cmdpipe
# Open sqlite3 with stdout assigned to fd 3
exec 3< <(sqlite3 "${path_to_db}" < sqlite3cmdpipe)

# Open command fifo for writing and assign fd 4
exec 4> sqlite3cmdpipe

# start the stopwatch
timestamp_start=$(date +%s%N)

# Let's talk to sqlite3
echo ".read ${path_to_current_script}" >&4
echo ".print SQLDone" >&4

#echo "Commands sent to sqlite3, waiting for done..."

# Read from sqlite3 stdout (fd 3) and wait for SQLDone. Using quiet to avoid printing data.
sed --quiet '/SQLDone$/q' <&3

# stop the stopwatch
timestamp_end=$(date +%s%N)

# calculate duration of query
realtime=$((timestamp_end-timestamp_start))

#echo "Done! Let's gather process statistics"

# get the sqlite process id
SQLITE_PID=$(pidof sqlite3)
echo "${SQLITE_PID}"

# allow time for the db to start up.
# sleep 0.5

# retrieve kernel and user execution time, add them up to total cpu time.
# https://man7.org/linux/man-pages/man5/proc.5.html 
# according to 'getconf CLK_TCK' (clock tick), the unit is 1/100 of a second. so 616 means 6.16 seconds.
process_stats=$(cat /proc/"${SQLITE_PID}"/stat)
utime=$(echo "${process_stats}" | cut -d ' ' -f 14)
stime=$(echo "${process_stats}" | cut -d ' ' -f 15)
cputime=$((utime+stime))
#echo ${cputime}

# get current time
current_time=$(date --iso-8601=seconds)

# Get peak memory usage (high water mark: VmHWM) in kB.
# https://ewx.livejournal.com/579283.html
mhwm=$(cat /proc/"${SQLITE_PID}"/status | grep -e "^VmHWM" | cut -f 2 -d ":" | tr -d '[:space:]')
vmhwm=${mhwm::-2}
#echo ${mhwm}
#echo ${vmhwm}

# Get amount of reads and writes in bytes.
# https://man7.org/linux/man-pages/man5/proc.5.html
io_disk_reads=$(cat /proc/"${SQLITE_PID}"/io | grep -e "^read_bytes" | cut -f 2 -d ':' | tr -d '[:space:]')
io_disk_writes=$(cat /proc/"${SQLITE_PID}"/io | grep -e "^write_bytes" | cut -f 2 -d ':' | tr -d '[:space:]')

# get name of flux script file
filename=$(basename "${path_to_current_script}")
extension="sql_log.csv"
logfile="${filename%.sql}"_"${extension}"

# write timestamp, script name, cpu time(centisec), memory_HWM(kB), disk reads, writes(bytes), realtime
echo "${current_time}","${filename}","${cputime}","${vmhwm}","$io_disk_reads","$io_disk_writes","$realtime"  >> "${logfile}"


echo "Gathered all data, terminating sqlite3 process."
# closing fd 4, causes end of file, terminating sqlite.
# https://stackoverflow.com/questions/3462075/keep-a-file-open-forever-within-a-bash-script
exec 4>&-
# Delete named pipe.
rm sqlite3cmdpipe

