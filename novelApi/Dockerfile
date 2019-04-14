FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /novelApi
WORKDIR /novelApi
COPY . /novelApi
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh && pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
