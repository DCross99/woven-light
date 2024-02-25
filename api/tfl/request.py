import requests


def call_to_tfl():
    r = requests.get('https://api.github.com/events')
