# import boto3
# athiva = boto3.client('s3')
# response = athiva.list_objects(
#     Bucket='athiva-training',Prefix='athiva5k/'
#
# )
#
# print(response)


from pathlib import Path
print(Path(r"C:\folder1\folder2\filename.xml").parts[0])