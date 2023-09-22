FROM python:3

ENV PYTHONUNBUFFERED 1

#RUN mkdir /sample
WORKDIR /sample
COPY requirements.txt  /sample/
RUN pip install -r requirements.txt
COPY . /sample/
CMD python run.py