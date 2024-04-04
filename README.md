# AWSCDK-Practice
# Structure: cdk-app/
<i>Codes while practicing AWS CDK. This one will install the CDK on CloudShell.</i>

`#install CDK
sudo npm install -g aws-cdk-lib
 
#create an app folder and go there
mkdir cdk-app
cd cdk-app/
 
#initialize the app
cdk init app --language <language>
#verify if it works
cdk ls
 
#copy the content of sample cdk-app-stack.js into lib/cdk-app-stack.js
cd lib/ #go to the lib/ directory
rm cdk-app-stack.js #delete it
touch cdk-app-stack.js #to create a new file
nano cdk-app-stack.js #edit it
 
#sample cdk-app-stack.js, copy the contents and save
 
#setup Lambda function
cd ..
mkdir lambda && cd lambda
touch index.py

#Paste the contentes of lambda/index.py

#bootsrap the CDK application
cd .. #go up to run the cdk.json
cdk bootstrap #you will do once per account per region

#Check CloudFormation to check the progress

#sythesize to get the target CloudFormation template that is going to be generated out of our stack.
#this will be sent to CloudFormation and we can preview it
cdk syth

#deploy the CDK stack
cdk deploy

#empty s3 bucket
#destroy the stack
cdk destroy`
