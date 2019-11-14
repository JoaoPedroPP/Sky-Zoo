FROM python:3.7.2-slim

WORKDIR /home/skyzoo

COPY . /home/skyzoo

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]