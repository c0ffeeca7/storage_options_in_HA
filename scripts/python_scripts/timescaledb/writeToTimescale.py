from datetime import datetime
from io import StringIO
import yaml
from yaml.loader import FullLoader # for user credentials config file
import psycopg2
from pgcopy import CopyManager
import csv
from typing import List, Tuple, Dict, Generator
import time

# the connection string. Format: postgres://username:password@host:port/dbname
# https://docs.timescale.com/timescaledb/latest/quick-start/python/#step-2-compose-a-connection-string
CONNECTION: str

# read connection datails from config file
def get_connection_info():
    """Return connection information for timescale."""

    # https://tutswiki.com/read-write-yaml-config-file-in-python/
    with open ("timescale_config.yml", "r") as yamlfile:
        config_data = yaml.load(yamlfile, Loader=FullLoader)
        host = config_data['timescaledb']['host']
        dbname = config_data['timescaledb']['database_name']
        username = config_data['timescaledb']['username']
        password = config_data['timescaledb']['password']
        port = config_data['timescaledb']['port']
        connect_timeout = config_data['timescaledb']['connect_timeout']
        Connection = f"postgres://{username}:{password}@{host}:{port}/{dbname}"
        print(f"hello {Connection}")
    return Connection  


# Create a connection string for timescaledb
# CONNECTION = "postgres://username:password@host:port/dbname"
CONNECTION :str = get_connection_info()

# connect to db
# use the cursor to interact with your database
        # cursor.execute("SELECT * FROM table")
conn = psycopg2.connect(CONNECTION)
cursor = conn.cursor()

# 
query_create_timescale_extension = "CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;"
# formulate create table statement for states table
# remove prinary key see https://stackoverflow.com/questions/61205063/error-cannot-create-a-unique-index-without-the-column-date-time-used-in-part
query_create_states_table = """CREATE TABLE states (created TIMESTAMP, value DOUBLE PRECISION, domain VARCHAR(64), entity_id VARCHAR(64), measurement VARCHAR(64));"""

# Formulate the SELECT statement to create the hypertable (required for timescale)
# converts the states table to a hypertable
query_create_states_hypertable = "SELECT create_hypertable('states', 'created');"

# formulate create table statement for states table
# remove prinary key see https://stackoverflow.com/questions/61205063/error-cannot-create-a-unique-index-without-the-column-date-time-used-in-part
query_create_test_table = """CREATE TABLE test (created TIMESTAMP, value DOUBLE PRECISION, domain VARCHAR(64), entity_id VARCHAR(64), measurement VARCHAR(64));"""

# Formulate the SELECT statement to create the hypertable (required for timescale)
# converts the states table to a hypertable
query_create_test_hypertable = "SELECT create_hypertable('test', 'created');"

# creates a states table in timescaledb. Schema is a reduced version of the current HA implementation.
# with 'state' being renamed to 'value', using double precision instead of string.
# Schema aims to be similar to the one used for TSDBs.
def createStatesTable(conn, cursor):
    cursor.execute(query_create_timescale_extension)
    cursor.execute(query_create_states_table)
    cursor.execute(query_create_states_hypertable)
    conn.commit()
    cursor.close()

def createTestTable(conn, cursor):
    cursor.execute(query_create_timescale_extension)
    cursor.execute(query_create_test_table)
    cursor.execute(query_create_test_hypertable)
    conn.commit()
    cursor.close()


def insertEnergyPointsFromFile(filename, conn):
    # initialize with some suspicious values
    value: float = 111.111
    timestamp = 163555666
    entity_id: str = "f9_phase"
    connection = conn
#etime.utc.unix,Phase1.Wh.d6,Phase2.Wh.d6,Phase3.Wh.d6,oven_power.Wh.d6,stove_power.Wh.d6,F6_Phase1.Wh.d6,F6_Phase3.Wh.d9
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
        
        # https://docs.python.org/3/library/typing.html
        # https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executemany (see example using a generator)
        # create a row generator: allows to add all rows in one transaction via cursor.executemany() (instead of writing line by line)
        def row_generator() -> Generator[Tuple[datetime, float, str, str, str], None, None]:
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
                        domain: str = "sensor"
                        measurement: str = "Wh"
                        data_tuple = (timestamp, value, domain, entity_id, measurement)
                        yield data_tuple
                        i += 1
                except ValueError:
                    missing_data.append(timestamp)
                    print(f"{timestamp}: no value at this time.")


        sql_statement = """INSERT INTO test (created,value,domain,entity_id,measurement) VALUES (%s,%s,%s,%s,%s);"""
       
        # https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executemany (see example using a generator)
        cursor.executemany(sql_statement, row_generator())
            #values = cursor.fetchall()
        #(Exception, psycopg2.Error) as error:
        #  print(error.pgerror)

        # Define columns of table to insert data into
        #cols = ['created', 'value', 'domain', 'entity_id', 'measurement']

        # Instantiate a CopyManager with target table and column definition
        #mgr = CopyManager(conn, 'states', cols)
        #mgr.copy(values)

        # save data
        connection.commit()  
        connection.close() 
        print(f"number of rows including null: {len(missing_data)}")
        # print(str(value) + " " + str(timestamp) + "" + str(entity_id))
    return True


# get the start time for stop watch
#print("starting data import...")
#start_time = time.time()
createStatesTable(conn, cursor)
#createTestTable(conn, cursor)
CONNECTION :str = get_connection_info()

conn = psycopg2.connect(CONNECTION)
cursor = conn.cursor()
#insertEnergyPointsFromFile('energy_data_testset.csv',  conn)
#end_time = (time.time() - start_time)
#print("import complete! --- %s seconds ---" % end_time)
# import complete! --- 14996.480348348618 seconds ---(=4.17 hours)

#def main():
#     print("hoihoi")
#     connection: sqlite3.Connection = create_connection(r"/var/www/html/repo/baa/dev/sqlite3db/pythonsqlite.db")
#     # setup states table
#     # https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3
    
        
#     # get the start time for stop watch
#     start_time = time.time()

      # create the states table in timescaledb  
#     createStatesTable(conn, cursor)
#
 #    insertEnergyPointsFromFile('energyData_00.csv',  connection)
#     end_time = (time.time() - start_time)

#     # get the time stamp when function has finished it work.
#     print("--- %s seconds ---" % end_time)


#if __name__ == '__main__':
 #   main()