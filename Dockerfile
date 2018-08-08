
FROM python:2.7-slim
WORKDIR /app
COPY helloworld.py requirements.txt /app/
RUN pip install --trusted-host pypi.python.org -r requirements.txt
ENV PORT 8080
CMD ["python", "helloworld.py"]
