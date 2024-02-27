FROM python:3.12.2-alpine
WORKDIR /api
ADD ./woven_light/api /api
RUN pip install -r api-requirements.txt
CMD ["python", "-u","app.py"]
