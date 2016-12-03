FROM python:2.7
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT DEV
ENV DWOLLA_SECRET 3EziUfefpqEtJL6ue0qZgppt55/w9txXCKufKdvTzqbeKVdxTd
ENV DJANGO_SECRET_KEY xYVoMG}Nc&qk37vr26h46`o/H47ggGNJLf6C)R3'!}gsT_2zea
ENV FERNET_KEY asimei28kac832klalk;8asdlk9mkahar;lkas8djklasjlfkasfdo0k
COPY requirements.txt /code/
#COPY familytree /code/familytree
COPY simplepyged/simplepyged /usr/local/lib/python2.7/site-packages/simplepyged/
WORKDIR /code
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt
