docker build -t httprunner .

docker run -it --rm --name demo-httprunner -v "$PWD":/usr/src/myapp -w /usr/src/myapp httprunner sh

hrun `pwd`/testcases/you-json-file.json

