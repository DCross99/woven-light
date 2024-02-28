FROM python:3.12.2-alpine
WORKDIR /tfl_scraper
ADD ./woven_light/tfl_scraper /tfl_scraper
RUN pip install -r tfl-scraper-requirements.txt
CMD ["python", "-u","main.py"]
