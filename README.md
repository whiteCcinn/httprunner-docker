## start

```
docker build -t httprunner .
```

## run single testcase

```
docker run -it --rm -v "$PWD":/usr/src/myapp httprunner testcases/you-json-file.json

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
