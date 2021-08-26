# kubernetes

## 安装方法

```
$ apt-get update && apt-get install -y apt-transport-https
$ curl https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | apt-key add - 
$ cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main
EOF  
$ apt-get update
$ apt-get install -y kubelet kubeadm kubectl
```

## 安装指定版本：
$ apt-get install kubeadm=1.10.2-00 kubectl=1.10.2-00 kubelet=1.10.2-00


#查看 Docker 版本
docker -v
sudo docker pull 仓库/镜像:版本（留空的话默认为 latest）
sudo docker run 加参数，用来创建容器
#查看运行容器
sudo docker ps
#查看所有下载的镜像
sudo docker images
#进入容器终端
sudo docker exec -i -t ha /bin/bash
#实时查看10行的 ha 日志
sudo docker logs -f -t --tail 10 ha
#重启 systemctl 守护进程
sudo systemctl daemon-reload
#设置 Docker 开机启动
sudo systemctl enable docker
#开启 Docker 服务
sudo systemctl start docker
 
#下载 Docker 图形化界面 portainer
sudo docker pull portainer/portainer
#创建 portainer 容器
sudo docker volume create portainer_data
#运行 portainer
sudo docker run -d -p 9000:9000 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer


# get started

## start the tutorial

docker run -d -p 80:80 docker/getting-started

You’ll notice a few flags being used. Here’s some more info on them:

    -d - run the container in detached mode (in the background)
    -p 80:80 - map port 80 of the host to port 80 in the container
    docker/getting-started - the image to use

## Our App

docker build -t getting-started .

docker run -dp 3000:3000 getting-started

## Updating Our App

docker ps 

docker stop c600818998cc

## Share our App

docker image ls

docker login -u

docker tag getting-started zhangle231/getting-started

docker push zhangle231/getting-started

## persisting our db

docker exec <container-id> cat /data.txt

container volumes

create a volume 

docker volume create todo-db

docker run -dp 3000:3000 -v todo-db:/etc/todos getting-started

docker run -dp 3000:3000 `
    -w /app -v "$(pwd):/app" `
    node:12-alpine `
    sh -c "yarn install && yarn run dev"