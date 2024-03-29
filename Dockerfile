FROM python:3.7-alpine
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 80

CMD ["ddtrace-run", "python", "send_trace.py"]
