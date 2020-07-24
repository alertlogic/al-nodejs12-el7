# alertlogic al-nodejs12-el7 rpm for centos7/amzn2

### to release changes to integration (pick one)
1. merge pull request (this will trigger rpm build and deployment to integration mirror list)
1. aws --region=us-east-1 --profile=dev-sysops-dsa codebuild start-build --project-name al-nodejs12-el7
