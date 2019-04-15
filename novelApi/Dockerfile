FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /novelApi
WORKDIR /novelApi
COPY . /novelApi
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
