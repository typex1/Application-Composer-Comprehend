# Application-Composer-Comprehend

* Login into AWS Console (using Chrome gives the best user experience for the Application Composer frontend)
* Download this repository to your local drive
* Go to the Region of you choice, switch to "Application Composer"
* On the dashboard, on the top right, choose Menu > Open > Project Folder
* Select the folder of this repository -> you will see that the icons of the different AWS resources will show up - they are extracted from the SAM template.yaml file
* Make sure you have SAM intalled on your commandline (otherwise refer to https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html
* cd into the repository directory, type "sam build" - this will build your sam project
* type "sam deploy" - this will deploy the infrastructure in your current Region
* See SAM policy templates here: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-policy-templates.html
