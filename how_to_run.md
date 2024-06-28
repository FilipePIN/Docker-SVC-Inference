### Sources:
#### https://docker-curriculum.com/
#### https://github.com/prakhar1989/docker-curriculum/tree/master/flask-app

### Build the image
- docker build -t svc-inference:test .
<!-- - docker build --platform linux/amd64 -t svc-inference:test . -->
- docker images

### Test image locally:

- docker run -p 9000:5000 svc-inference:test
<!-- - docker run -dp 9000:8080 svc-inference:test -->
<!-- - docker run --platform linux/amd64 -p 9000:8080 svc-inference:test -->
- curl "http://localhost:9000/" -d '{"payload":"hello world!"}'
<!-- - curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"payload":"hello world!"}' -->
- docker ps
- docker kill <container_id>
- docker stop <container_id>
- docker rm <container_id>
- docker rmi -f <image_id>
- docker system prune -a