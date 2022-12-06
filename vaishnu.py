import boto3
s3 = boto3.resource('s3')
response=s3.Bucket('athiva-training')

for list in response.objects.all():
    print(list.key)



