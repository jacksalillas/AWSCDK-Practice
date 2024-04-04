# AWSCDK-Practice
# Structure: cdk-app/
<i>Codes while practicing AWS CDK. This one will install the CDK on CloudShell.</i>

<code>#install CDK
sudo npm install -g aws-cdk-lib</code>
 
<code>#create an app folder and go there
mkdir cdk-app
cd cdk-app/</code>
 
<code>#initialize the app
cdk init app --language <language>
#verify if it works
cdk ls</code>
 
<code>#copy the content of sample cdk-app-stack.js into lib/cdk-app-stack.js
cd lib/ #go to the lib/ directory
rm cdk-app-stack.js #delete it
touch cdk-app-stack.js #to create a new file
nano cdk-app-stack.js #edit it</code>
 
<code>#sample cdk-app-stack.js, copy the contents and save</code>
 
<code>#setup Lambda function
cd ..
mkdir lambda && cd lambda
touch index.py</code>

<code>#Paste the contentes of lambda/index.py</code>

<code>#bootsrap the CDK application
cd .. #go up to run the cdk.json
cdk bootstrap #you will do once per account per region</code>

<code>#Check CloudFormation to check the progress</code>

<code>#sythesize to get the target CloudFormation template that is going to be generated out of our stack.
#this will be sent to CloudFormation and we can preview it
cdk syth</code>

<code>#deploy the CDK stack
cdk deploy</code>

<code>#empty s3 bucket
#destroy the stack
cdk destroy</code>
