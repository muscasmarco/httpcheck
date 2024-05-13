# httpcheck
A very simple docker container for testing NGINX configurations.

## Build and deploy

### Prerequisites
Install docker on the hosting machine. If you're me, then you should already have it installed :)

### Build
First, build the image:
    
    docker build -t muscasmarco/httpcheck -f Dockerfile .

Then deploy it using the Docker compose. 

    docker compose up -d
