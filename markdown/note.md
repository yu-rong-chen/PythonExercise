# Docker

What is dockerfile, image and container?
    ![Docker,diagram](image/docker_sketch.png)

## Create DockerFile on workstation

## build command 

Build image conmmand:`docker build -t $name .`

List all image: `docker images`

Remove all images: `docker rmi $(docker images -aq)`


## Push DockerFile to Dockerhub or Github

* Get token from Github

    Get token from github first
        ![Generate token](image/Get_token.png)
    Docker login command: `docker login -u yu-rong-chen -p $token_id docker.pkg.github.com`

* Create repository on Docker Hub

    Error will pop if user didn't login:
    
        "You have reached your pull rate limit. You may increase the limit by authenticating and upgrading: https://www.docker.com/increase-rate-limit"
        
    ![image](https://user-images.githubusercontent.com/52913327/173291575-d0bca5d8-c9e7-4061-8a9c-93a907050b80.png)
    
    Log in Docker: `docker login ` and enter Docker Hub username and password
    Push to repository `docker push $Hub_username/$repository `

If docker push failed, you need to tag first
    ![Docker,push failed](image/docker_push_failed.png)

Command: `docker tag $ImageID $username/$repository`
    ![docker image](image/docker_after_tag.png)

## Choose project from Github to build 

## Build Commences

## Docker image get ready for the pull

## Docker Run

List container command:
`$docker ps –a`

Start container command: \
`$docker run --name $ContainerName`\
`docker run -t -d --name $ContainerName ${ImangeName}`

Start container and execute job command: 
`$docker run --name $ContainerName $ImageName robot test.robot`

Create a container and start a Bash session
`$docker run --name $ContainerName --rm -i -t $ImageName bash`

Try another command:

`$docker run -d -p 80:81 $ImageName `

Remove all containers: `docker rm $(docker ps -aq)`

Start an exist container: `docker start ${container name}`

Start a bash session in that container: \
`$docker exec -it ${container name} bash`\
`$docker exec -it $ContainerID /bin/bash`

## Run the container from the image on workstation


## Docker Compose
[Flask 實作 Docker-compose (Flask+Nginx+PostgreSQL)](https://www.maxlist.xyz/2020/06/14/flask-docker-compose/)\
`$docker-compose up --build`
