## Visualisation of Epidemic

This is a demo streamlit WebApp deployed with Docker.

To deploy the App, please follow the instructions below.

$ docker build -f Dockerfile -t app:latest .

$ docker run -p 80:8501 -d app:latest

Then the docker container will be running in the background.

Please note that editing source files will not change anything in the container if volume function is not used. You need to destroy this and build a new one to edit the App.

To destroy the App, please follow the instructions below.

$ docker ps -a

$ docker kill ContainerID

$ docker rm ContainerID

$ docker images

$ docker rmi ImageID
