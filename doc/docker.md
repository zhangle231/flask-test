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
