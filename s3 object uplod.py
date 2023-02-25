import boto3
session = boto3.Session(profile_name='vaishnu-dev-profile')
dev_s3_client = session.client('s3')

dev_s3_client.upload_file('C:/Users/vaish/OneDrive/Desktop/sso_setup.txt', 'vaishnu-files', 'sso_setup.txt')




















# import boto3
#
# # create an S3 client
# s3 = boto3.client('s3')
#
# # upload a file to S3
# bucket_name = 'vaishnu-files'
# file_path = '"C:/Users/vaish/OneDrive/Desktop/sso_setup.txt"'
# object_name = 'sso_setup.txt'
#
# # use the put_object() method to upload the file
# with open("C:/Users/vaish/OneDrive/Desktop/sso_setup.txt", "rb") as f:
#     s3.put_object(Bucket='vaishnu-files', Key=object_name, Body=f)