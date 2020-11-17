FROM python:3.7
WORKDIR /application
COPY . .
RUN pip install -r requirements.txt
ENV  'DB_URI'='sqlite:///'
ENV 'SECRET_KEY'=''
RUN python create.py
EXPOSE 5000
ENTRYPOINT ["python","app.py"]

