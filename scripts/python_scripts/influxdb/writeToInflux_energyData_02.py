from datetime import datetime
from typing import List

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS, WriteOptions, WriteType
import get_connection_to_Influxdb

import csv

# script to write energy data to InfluxDB.
# requires energyData.csv in the follwoing format:
# time, phase1, phase2, phase3, oven_power, stove_power, dryer_power, washing_machine_power
# 1605355200, 0.323324265, 0.05500192, 0.132076006, 0.001605388, 0.00256584, 0.000528204, 0.001562356

client = get_connection_to_Influxdb.get_connection()
bucket = get_connection_to_Influxdb.get_bucket_and_org()[0]
org = get_connection_to_Influxdb.get_bucket_and_org()[1]
write_api = client.write_api(write_options=WriteOptions(write_type=WriteType.batching, batch_size=6000, flush_interval=6000))

# reads data point from csv and writes them to influxdb.
def importEnergyPointsFromFile(filename, write_func) -> bool:
    value: float = 444.444
    timestamp = 1636553656
    entity_id: str = "f3_phase"


    with open(filename, 'r') as f:
        csvReader = csv.reader(f, delimiter=',')
         # extract the header information from the first row
        header = next(csvReader)
        numberOfColums = len(header)
        print(f"number of colums: {numberOfColums}")
        # move to the second row, where the payload starts
        next(csvReader)        
        entity_id = header[1]
        # list to collect the timestamps with associated null values
        missing_data : List[int] = []
       
        for row in csvReader:
            try:
                i = 1
                # do this for each column (except the 1st one with the timestamp)
                while(i < numberOfColums):
                    #https://docs.python.org/3/library/datetime.html                    
                    timestamp = datetime.fromtimestamp(int(row[0]))
                    entity_id = str.strip(header[i])
                    # print(row[i])
                    value = float(row[i])                                            
                    #data_tuple = (timestamp, value, domain, entity_id, measurement)
                    writeEnergyPointToInfluxDB(timestamp, value, entity_id)
                    i += 1
            except ValueError:
                missing_data.append(timestamp)
                print(f"{timestamp}: no value at this time.")
        print(len(missing_data))
        # Flush data and dispose of batching buffer.
        print("writing complete")
        write_api.close()


#https://gist.github.com/noahcrowley/941e87422cd6fc43b0e9e8f0d0877836/#file-write_test-py
def writeEnergyPointToInfluxDB(timestamp:datetime, value: float, entity_id: str) -> bool :

    measurement: str = "Wh"
    domain: str = "sensor"
    channel:str = ""
    device_class_str:str = "energy"
    friendly_name_str:str = "total_energy"
    state_class_str:str = "measurement"
    last_type_str:str = "output"
    value:float = value
    timestamp:datetime = timestamp
    entity_id: str = entity_id


# point.field("channel", channel)
    # point.field("device_class_str", device_class_str)
    # point.field("friendly_name_str", friendly_name_str)
    # point.field("state_class_str", state_class_str)
    # point.field("last_type_str", last_type_str)
    # define a data point
    # https://influxdb-client.readthedocs.io/en/stable/api.html#writeapi
    
    point = Point.measurement(measurement)
    point.tag("domain", domain)
    point.tag("entity_id", entity_id)    
    point.field("value", value)
    point.time(timestamp, write_precision = WritePrecision.S)

    # write point to influxdb
    ret = write_api.write(bucket, org, point)
    #print(ret)


    return True

importEnergyPointsFromFile('energyData.csv', writeEnergyPointToInfluxDB)
