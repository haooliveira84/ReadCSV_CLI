FROM python:alpine

LABEL Name=devops-challange Version=2.0.1
    
    COPY ./app /app
    WORKDIR /app
    ADD . /app

    ENTRYPOINT ["python"]
    # Using pip:
    RUN python -m pip install -r requirements.txt
    CMD ["app.py"]