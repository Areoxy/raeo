import requests


def get__ip():
    r = requests.get("http://ip-api.com/json/")
    result = r.json()

    ip = result['query']
    country = result['country']
    city = result['city']
    region = result['regionName']
    isp = result["isp"]
    return [ip, country, city, region, isp]