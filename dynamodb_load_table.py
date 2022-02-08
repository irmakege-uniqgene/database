import json  # module for converting Python objects to JSON
# decimal module support correctly-rounded decimal floating point arithmetic.
from decimal import Decimal
import boto3  # import Boto3


def load_data(genome, dynamodb=None):
    dynamodb = boto3.resource(
        'dynamodb')

    genome_table = dynamodb.Table('genome_table')
    # Loop through all the items and load each
    for g in genome:
        team_id = (g['team_id'])
        datacount = g['datacount']
        # Print device info
        print("Loading Gene Data:", team_id, datacount)
        genome_table.put_item(Item=g)


if __name__ == '__main__':
    # open file and read all the data in it
    with open("data.json") as json_file:
        genome_list = json.load(json_file, parse_float=Decimal)
    load_data(genome_list)