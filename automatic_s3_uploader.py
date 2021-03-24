from secrets import access_key, secret_access_key

import boto3
import os

client = boto3.client('s3',
                        aws_access_key_id=access_key,
                        aws_secret_access_key=secret_access_key)


ext = input('What kind of extension would you like to upload [i.e. pdf]: ')
ext = '.' + ext.lower()
for file in os.listdir():
    if ext in file:
        # IMPORT AWS BUCKET NAME HERE
        upload_file_bucket = ''
        # YOU CAN CHANGE DIRECTORY NAME FROM 'python/'
        upload_file_key = 'python/' + str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)
