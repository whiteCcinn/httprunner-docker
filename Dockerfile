FROM python:3.6-alpine3.6

ENV HTTPRUNNER_VERSION 1.5.10
ENV PYTHON_VERSION 3.6
ENV WORKSPACE /usr/src/myapp

RUN echo -e "http://mirrors.ustc.edu.cn/alpine/v3.7/main\nhttp://mirrors.ustc.edu.cn/alpine/v3.7/community" > /etc/apk/repositories && \
    apk update && \
    apk add wget && \
    apk add vim

RUN echo -e "${WORKSPACE}" > /usr/local/lib/python${PYTHON_VERSION}/site-packages/httprunner.pth

WORKDIR ${WORKSPACE}

COPY . .

RUN pip install --no-cache-dir -r requirements.txt && \
    ln -s $(pwd)/docker-entrypoint.sh /usr/local/bin/ && \
    chmod +x /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["sh", "docker-entrypoint.sh"]

CMD ["hrun", "-h"]
