import boto3
session = boto3.Session(profile_name='vaishnu-dev-profile')

# Create a Glue client in the ap-south-1 region
glue_client = session.client('glue', region_name='ap-south-1')

# Call the get_databases method to retrieve a list of databases
response = glue_client.get_databases()

for database in response['DatabaseList']:
    print(database['Name'])