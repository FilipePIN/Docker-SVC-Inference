### Docker Image Generator Mock

#### Build the image:
- docker build -t image-generator:test .
- docker images

#### Test image locally:

- docker run image-generator:test
<!-- - docker run -p 9090:6000 image-generator:test -->

#### Util commands:

- docker ps
- docker kill <container_id>
- docker stop <container_id>
- docker rm <container_id>
- docker rmi -f <image_id>
- docker system prune -a