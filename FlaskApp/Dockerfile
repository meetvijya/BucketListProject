FROM python:3.7.1

WORKDIR /BucketListProject
RUN pip install flask
RUN pip install werkzeug
RUN pip install flask-MySQL
RUN pip install --upgrade pip
RUN pip install cryptography

COPY . ./

#Set environment variables fo Flask
#ENV FLASK_APP = app.py
#ENV FLASK_ENV =  development
#ENV FLASK_RUN_HOST = 0.0.0.0
#ENV FLASK_RUN_PORT = 5001
 
EXPOSE 5001

CMD [ "python", "app.py"]