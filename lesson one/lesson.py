import boto3
import json

AccessKey='Enter your Accesskey here'
SecretKey='Enter your Secretkey here'


"""    Program to get instance running in any region """
"""  it will help to not required to get any region statically """

ec2 = boto3.Session(region_name="us-east-1",aws_access_key_id=AccessKey,aws_secret_access_key=SecretKey)
client = ec2.client(service_name='ec2')
all_regions = client.describe_regions()

list_of_all_regions=[]
for nehru in all_regions["Regions"]:
    list_of_all_regions.append(nehru["RegionName"])
 
for each_region in  list_of_all_regions:
    ec2_instance=boto3.resource('ec2',each_region,aws_access_key_id=AccessKey,aws_secret_access_key=SecretKey)
    for ec2ins in ec2_instance.instances.all():
       for nehru in ec2ins.tags:
           if nehru["Key"] == "Name":
                print(ec2ins.id, ec2ins.private_ip_address,nehru["Value"],ec2ins.state["Name"],ec2ins.instance_type,each_region)
                