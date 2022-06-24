FROM python:3.8.6

RUN apt-get update \
&& apt-get install -y postgresql postgresql-contrib libpq-dev python3-dev

RUN pip3 install --upgrade pip

COPY ./ ./
RUN pip3 install -r requirements.txt

RUN rm ./TODO/venv/lib/python3.8/site-packages/graphene_django/utils/utils.py
COPY /home/lina/PycharmProjects/TODO/venv/lib/python3.8/site-packages/graphene_django/utils/utils.py /home/lina/PycharmProjects/TODO/venv/lib/python3.8/site-packages/graphene_django/utils/utils.py
COPY wait-for-postgres.sh .
RUN chmod +x wait-for-postgres.sh
RUN pip3 install gunicorn
