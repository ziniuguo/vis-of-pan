## Visualisation of Epidemic

Demo

<img src="Screenshot1.png" width=40% height=40%>

To deploy

$ docker build -f Dockerfile -t app:latest .

$ docker run -p 80:8501 -d app:latest



To destroy

$ docker ps -a

$ docker kill ContainerID

$ docker rm ContainerID

$ docker images

$ docker rmi ImageID
