## Docker Image Processing Mock

#### Build the image:
- docker build -t image-processing:test .
- docker images

#### Test image locally:

- docker run image-processing:test
<!-- - docker run -p 9090:6000 image-processing:test -->

#### Util commands:

- docker ps
- docker kill <container_id>
- docker stop <container_id>
- docker rm <container_id>
- docker rmi -f <image_id>
- docker system prune -a