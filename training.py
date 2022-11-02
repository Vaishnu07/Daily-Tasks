import boto3
import glob
import os

athiva = boto3.client('s3')
employee=glob.glob('vaishnu/*')
for department in employee:
     path=(os.path.basename(department))
     print(path)
     response = athiva.upload_file(department, 'athiva-training','vaishnu/'+ path)
     print(response)