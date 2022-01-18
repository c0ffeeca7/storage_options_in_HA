from datetime import datetime
from io import StringIO
import sqlite3
from sqlite3 import Error
import csv
from typing import List, Tuple, Dict, Generator
import time

# Sets up a connection to an SQLitedb file. Creates the file if not exists.
def create_connection(db_file) -> sqlite3.Connection:
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)    
    return conn

# creates a states table in the SQLitedb. Schema is a reduced version of the current HA implementation.
# with 'state' being renamed to 'value', using FLOAT instead of string.
# Schema aims to be similar to the one used for TSDBs.
def createStatesTable(conn: sqlite3.Connection):
    connection = conn
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE states (state_id INTEGER NOT NULL,	created DATETIME, value FLOAT, domain VARCHAR(64), entity_id VARCHAR(64), measurement VARCHAR(64), PRIMARY KEY (state_id))")

def readEnergyPointsFromFile(filename, conn: sqlite3.Connection) -> bool:
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


        sql_statement = "INSERT INTO states (created, value, domain, entity_id, measurement) VALUES (?, ?, ?, ?, ?)"
        cursor = connection.cursor()
        # https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executemany (see example using a generator)
        cursor.executemany(sql_statement, row_generator())
        


        # save data
        connection.commit()  
        connection.close() 
        print(len(missing_data))
        # print(str(value) + " " + str(timestamp) + "" + str(entity_id))
    return True


# writes the data to SQLitedb, into the states table
def writeDataToSQLiteStatesTable(value: float , timestamp:datetime, entity_id: str, cursor: sqlite3.Cursor) -> bool :
    
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
    # tate_id INTEGER NOT NULL,	created DATETIME, value FLOAT, domain VARCHAR(64), entity_id VARCHAR(64), PRIMARY KEY (state_id))"
    # define a data point
    datapoint = "INSERT INTO states (created, value, domain,entity_id,measurement) VALUES (?, ?, ?, ?, ?)"
    # write data point into states table in the SQLite database 
    
    cursor.execute(datapoint, (timestamp, value, domain, entity_id, measurement))
    
    

    return True


def main():
    print("hoihoi")
    connection: sqlite3.Connection = create_connection(r"/var/www/html/repo/baa/dev/sqlite3db/pythonsqlite.db")
    # setup states table
    # https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3
    

    # get the start time for stop watch
    start_time = time.time()

    # createStatesTable(connection)
    readEnergyPointsFromFile('energyData_00.csv',  connection)
    end_time = (time.time() - start_time)

    # get the time stamp when function has finished it work.
    print("--- %s seconds ---" % end_time)


if __name__ == '__main__':
    main()