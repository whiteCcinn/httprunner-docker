FROM python:3.6-alpine3.6

WORKDIR /usr/src/myapp

RUN echo -e "http://mirrors.ustc.edu.cn/alpine/v3.7/main\nhttp://mirrors.ustc.edu.cn/alpine/v3.7/community" > /etc/apk/repositories && \
    apk update && \
    apk add wget && \
    apk add vim

COPY . .

RUN cp -v ./httprunner.pth /usr/local/lib/python3.6/site-packages/ && \
    pip install --no-cache-dir -r requirements.txt

CMD [ "python" ]
