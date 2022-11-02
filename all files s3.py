import boto3

service = boto3.client('s3')

response = service.list_objects(Bucket='athiva-training')

result = []
for key in (response['Contents']):
    # print(key)
    # print(type(key))
    key_values = key['Size'], key['Key']
    result.append(key_values)
arange = result

for i in range(len(arange)):
   # print(i)

   for j in range(i + 1, len(arange)):

       # if arange[i] > arange[j]:

           # arange[i], arange[j] = arange[j], arange[i]

#mini = arange[3]
#for i in arange:
 #  if i <= mini:


       # print("The Lowest fie is:", i)


