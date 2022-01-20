import requests


def send_requests(url):
    r = requests.get(url)
    return r.status_code


def visit_ustack():
    return send_requests('http://www.ustack.com')
