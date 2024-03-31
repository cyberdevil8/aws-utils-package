import boto3

def list_buckets():
    s3_client = boto3.client('s3')
    response = s3_client.list_buckets()
    buckets_info = []
    for bucket in response['Buckets']:
        bucket_name = bucket['Name']
        location = s3_client.get_bucket_location(Bucket=bucket_name)['LocationConstraint']
        account_id = boto3.client('sts').get_caller_identity().get('Account')
        buckets_info.append({
            'BucketName': bucket_name,
            'Region': location if location != 'US' else 'us-east-1',
            'AccountId': account_id
        })
    return buckets_info

