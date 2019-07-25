FROM python:3.6.5

# MAINTAINER
MAINTAINER tangle@meb.cn

ENV LANG C.UTF-8
ENV TZ=Asia/Shanghai

RUN apt-get update -y && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    apt-get install -y tzdata && \
    apt-get install -y python-pip python-dev

RUN pip install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com flask==1.0.2 && \
    pip install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com tornado==5.1.1 && \
    pip install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com beautifulsoup4==4.8.0 && \
    pip install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com zhon==1.1.5 && \
    pip install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com jieba==0.39 && \
    pip install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com requests=2.22.0


ADD ./codes /opt/topic-model/codes

WORKDIR /opt/topic-model/codes
