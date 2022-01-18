import yaml
from yaml.loader import FullLoader # for user credentials config file
from datetime import datetime

from influxdb_client import InfluxDBClient

# requires config.yml with predefined org, token, bucket. 
# org, token and bucket must already exist in InfluxDB.

###
# Start Database Section
###

# establish connection to influxdb container. Returns an InfluxDBClient.
def get_connection() -> InfluxDBClient:

    # https://tutswiki.com/read-write-yaml-config-file-in-python/
    with open ("config.yml", "r") as yamlfile:
        config_data = yaml.load(yamlfile, Loader=FullLoader)
        org = config_data['influxdb_client']['org']
        token = config_data['influxdb_client']['token']
        bucket = config_data['influxdb_client']['bucket']
        print("InfluxDB database configuration read successful")
        
    print(org)
    client = InfluxDBClient(url="http://localhost:8086", token=token, org=org)
    return  client

# return tuple of bucket and org name.
def get_bucket_and_org() -> tuple:

    # https://tutswiki.com/read-write-yaml-config-file-in-python/
    with open ("config.yml", "r") as yamlfile:
        config_data = yaml.load(yamlfile, Loader=FullLoader)
        bucket = config_data['influxdb_client']['bucket']
        org = config_data['influxdb_client']['org']
    return  bucket, org



###
# End Database Section
###


