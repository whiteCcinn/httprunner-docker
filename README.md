
### 1. 安装docker

略过....

### 2. 下载项目

```
git clone https://github.com/whiteCcinn/httprunner-docker.git
```

### 3. 进入项目

```
cd httprunner-docker
```

### 4. 编译dockerfile生成项目镜像

```
docker build -t httprunner .
```

### 5. 通过镜像运行容器代替httprunner

```
docker run -it --rm -v "$PWD":/usr/src/myapp httprunner
```

### 6. 运行demo

```
docker run -it --rm -v "$PWD":/usr/src/myapp httprunner ./testcases/demo.json
```

---

## run single testcase

```
docker run -it --rm -v "$PWD":/usr/src/myapp httprunner testcases/you-json-file.json

docker run -it --rm -v "$PWD":/usr/src/myapp httprunner ./testcases/you-json-file.json

docker run -it --rm -v "$PWD":/usr/src/myapp httprunner hrun testcases/you-json-file.json
```

## run all testcase

```
docker run -it --rm -v "$PWD":/usr/src/myapp httprunner run-all.sh
```

## login the container

``` 
docker run -it --rm -v "$PWD":/usr/src/myapp httprunner /bin/sh
```

--- 

All Detail please read my blog:[[ccinn 's blog - httprunner-docker]](https://usblog.crazylaw.cn/index.php/archives/428/)