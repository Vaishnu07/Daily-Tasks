import boto3
athiva = boto3.client('s3')
response = athiva.list_objects( Bucket='athiva-training')
number=[]
for object_list in (response['Contents']):
   # print(type(object_list))
    objects = object_list['Size'],object_list['Key']
    number.append(objects)
all_files = number

for value1 in range(len(all_files)):
   # print(value1)

   for value2 in range(value1 + 1, len(all_files)):
      # print((value2))
      # print(all_files[value1])
      # print(all_files[value2])
       if all_files[value1] > all_files[value2]:
           all_files[value1], all_files[value2] = all_files[value2], all_files[value1]
#store = all_files[3]
#for small in all_files:
   #if small <= store:
     #  print("The low size file is:", small)
      # print(type(small))
store = all_files[0]
for large in all_files:
        if large > store:
            store = large
print("The Largest File is:",store)
print(type(large))






