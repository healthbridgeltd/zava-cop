# Docker & AWS

This is an example for how you simply try something out in AWS.
This is not how you would run a production service!

## Make sure you have AWS cli configure

You need to have a `~/.aws/credentials` file similar to this:

```
[default]
aws_access_key_id = AKID1234567890
aws_secret_access_key = MY-SECRET-KEY
```

# Let's start

```
# create a machine
docker-machine create --driver amazonec2 --amazonec2-region eu-west-1 aws-sandbox

docker-machine ls
# make it active
eval $(docker-machine env aws-sandbox)
# do stuff
# then
docker-machine kill aws-sandbox
```