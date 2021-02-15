import sagemaker

input_bucket = 'eegdatabucket'
client = '7'
output_bucket = 'eegdatabucket'

estimator = sagemaker.estimator.Estimator(
                       image_uri='186524214904.dkr.ecr.us-east-1.amazonaws.com/sagemaker-images:GCN_train',
                       role='sagemakerfullaccessrole', 
                       instance_count=1, 
                       instance_type='ml.p3.2xlarge',
                       )

estimator.set_hyperparameters(input_bucket=input_bucket, client=client, output_bucket=output_bucket)

estimator.fit()