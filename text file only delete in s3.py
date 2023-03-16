# import boto3
# session = boto3.Session(profile_name='vaishnu-dev-profile')
# s3 = session.client('s3')
# bucket_name = 'vaishnu-files'
# response = s3.list_objects_v2(Bucket=bucket_name)
# for obj in response['Contents']:
#     key = obj['Key']
#     if key.endswith('.txt'):
#         print(f"Found file: {key}")
#         s3.delete_object(Bucket=bucket_name, Key=key)
        






# ----------------------------------------- Local folder /.textfile list using python

# import os
# import glob
#
# def readFromCorpus(directory_path):
#     os.chdir(directory_path)
#     for fu in glob.glob("*.txt"):
#         print('\n\n'+fu)
#         with open(fu,'r') as f:
#             data = f.readlines()
#             for line in data:
#                 print(line.replace('\n',''))
#
# # Call the function with the directory path
# readFromCorpus("C:/Users/vaish/OneDrive/Desktop/vaishnu2023")
