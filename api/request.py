import requests

JSON_HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'text/plain'
}


class Request:
    def __init__(self, url):
        self.url = url

    def get(self, path, **kwargs):
        return Request.get_content(requests.get(f'{self.url}{path}', **kwargs))

    def post(self, path, **kwargs):
        return Request.get_content(requests.post(f'{self.url}{path}', **kwargs))

    def put(self, path, **kwargs):
        return Request.get_content(requests.put(f'{self.url}{path}', **kwargs))

    def delete(self, path):
        return Request.get_content(requests.delete(f'{self.url}{path}'))

    @staticmethod
    def get_content(response):
        return response.json()
