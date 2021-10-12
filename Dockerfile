FROM python:3.8-slim-buster

ENV FLASK_APP="app.py"

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

#to build an image run this command:
# docker build -t bricbuddy .

#to run the application use this command:
# docker run -p 5000:5000 --name bricbuddy bricbuddy