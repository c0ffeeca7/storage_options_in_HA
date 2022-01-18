# Comparing storage options in Home Assistant

This repository contains the scripts and data files used in the BA Thesis "Comparing Storage Options in Home Assistant".
The aim of the thesis is to see if a time series database could provide any advantages to [Home Assistant](https://www.home-assistant.io/) (HA) in terms of processing time and resource consumption when used on a single board computer (such as a Raspberry&nbsp;Pi).

In the study, the following systems and tables are compared:

* SQLite states table (similar to states table in HA, but using a simplified schema)
* SQLite statistics table (similar to long term statistics table in HA, but using a simplified schema)
* InfluxDB
* TimescaleDB

The following performance metrics were compared: 

* CPU time
* actual duration of the query (wall clock time)
* memory usage (high water mark)
* amount of I/O reads

## **config** folder

Contains the configuration files for TimescaleDB (Postgres extension).
For InfluxDB and SQLite the default config was used.

## **measurements** folder

Contains the measurement results. 
The csv headers are:

timestamp, script_name, cpu_time_(s), memory_HWM_(MiB), disk_IO_reads_(MiB), disk_IO_writes_(MiB), wallclock_time_(s)

## **scripts** folder

Contains the scripts that were used to perform the quantitative tests.

* SQL and Flux queries
* python scripts used to import data to the databases
* python script to draw boxplots to present the final result
