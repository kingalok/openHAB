import boto3
import random

dynamodb = boto3.client('dynamodb')


def lambda_handler(event, context):
 
      customerid = 'cust' + str(random.randrange(1,999))
      path = 'Infra/AWS/customers/' + customerid + '/test.txt'
      dynamodb.put_item(TableName='customer', Item={"CustomerID": {"S": customerid },"CustomerName": {"S": "Mario"},"Date": {"S": "13-12-2022"}})
      client = boto3.client('codecommit')
      commit_id = client.get_branch(
      repositoryName='openHAB',
      branchName='main')['branch']['commitId']

      print('Alok sharma  debug: ' + commit_id)
      # client.put_file(repositoryName='openHAB', branchName='main', fileContent=b'bytes', filePath='string', fileMode='EXECUTABLE'|'NORMAL'|'SYMLINK',
      #                 parentCommitId='string', commitMessage='string', name='string', email='string')
      client.create_commit(
            repositoryName= 'openHAB',
            branchName= 'main',
            authorName= 'Alok',
            parentCommitId= commit_id,
            email= 'mailaloksharma@gmail.com',
            commitMessage= 'Testing',
            keepEmptyFolders=True,
            putFiles=[
                {
                    'filePath': path,
                    'fileContent': 'file_content'
                }
            ]
        )
      # client.create_branch( repositoryName='openHAB', branchName= customerid  , commitId= commit_id )