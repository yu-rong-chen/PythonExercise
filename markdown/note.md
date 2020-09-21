# Create DockerFile on workstation

## build command 

`docker build -t $name .`

## Push DockerFile to Github

Create repository on Docker Hub
Log in Docker `docker login ` and enter Docker Hub username and password
Push to repository `docker push $username/$repository `

Failed, need to tag first
    ![Docker,push failed](image/docker_push_failed.png)

Command: `docker tag $ImageID $username/$repository`
    ![docker image](image/docker_after_tag.png)

## Choose project from Github to build 

## Build Commences

## Docker image get ready for the pull

## Run the container from the image on workstation