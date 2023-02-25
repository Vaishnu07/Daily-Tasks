
import boto3

session = boto3.Session(profile_name='vaishnu-dev-profile')

bucket_name = 'vaishnu-files'

# Create an S3 resource
s3 = session.resource('s3')

# Select the bucket
bucket = s3.Bucket('vaishnu-files')

# Delete all objects in the bucket
bucket.objects.all().delete()

print(f"All objects in the '{'vaishnu-files'}' bucket have been deleted.")
