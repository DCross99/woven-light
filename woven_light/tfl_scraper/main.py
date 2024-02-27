import requests


def main():
    base_url = (
        "https://api.tfl.gov.uk/Line/bakerloo,jubilee,victoria,central,tram/Disruption"
    )

    response = requests.get(base_url)
    print(response.request)
    data = response.text
    if len(data) != 0:
        print(data)

    print("No Disruption")
