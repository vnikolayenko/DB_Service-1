from __future__ import print_function  # Python 2/3 compatibility

import os
import boto3

dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id="anything",
                          aws_secret_access_key="anything",
                          region_name=os.environ['region'],
                          endpoint_url=os.environ['db_url'])

table = dynamodb.create_table(
    TableName='Employees',
    KeySchema=[
        {
            'AttributeName': 'types',
            'KeyType': 'HASH'  #Partition keygit
        },
        {
            'AttributeName': 'emp_id',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'types',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'emp_id',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)