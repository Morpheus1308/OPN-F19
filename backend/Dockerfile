FROM python:3.7-alpine
WORKDIR /code
RUN pip install Flask
RUN pip install mysql-connector-python
ADD . /code
CMD python3 ./backend.py