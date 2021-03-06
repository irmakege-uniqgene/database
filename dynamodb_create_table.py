import boto3

dynamodb = boto3.resource('dynamodb')

import boto3  # import Boto3

def create_devices_table(dynamodb=None):
    dynamodb = boto3.resource('dynamodb')
    # Table defination
    table = dynamodb.create_table(
        TableName='genome_table',
        KeySchema=[
            {
                'AttributeName': 'team_id',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'datacount',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'team_id',
                # AttributeType defines the data type. 'S' is string type and 'N' is number type
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'datacount',
                'AttributeType': 'N'
            },
        ],
        ProvisionedThroughput={
            # ReadCapacityUnits set to 10 strongly consistent reads per second
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10  # WriteCapacityUnits set to 10 writes per second
        }
    )
    return table


if __name__ == '__main__':
    device_table = create_devices_table()
    # Print tablle status
    print("Status:", device_table.table_status)