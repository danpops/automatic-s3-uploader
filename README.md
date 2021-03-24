# Automatic S3 Uploader via Python3

Automatic S3 Uploader is a Python script handles different files (based on user inputted extension file type) which are automatically uploaded to Amazon S3. In order to use this, you must have your AWS access key id and AWS secret key. 

## Installation

In order to use this script, you must use Python 3 and have boto3 installed:

```bash
pip3 install boto3
```

You can then run the script. Ensure all the files you are uploading are located in the same folder as your automatic_s3_uploader.py and secrets.py files. 

```bash
python3 automatic_s3_uploader.py
```

