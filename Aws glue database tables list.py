import boto3

session = boto3.Session(profile_name='vaishnu-dev-profile')

glue_client = session.client('glue')

database_name = 'customer_analytics'

response = glue_client.get_tables(DatabaseName=database_name)
# print(response)


for table in response['TableList']:
    print(table['Name'])