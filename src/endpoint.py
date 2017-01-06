import json

import requests


class HttpEndpoint:
    """ Encapsulates HTTP endpoint details """

    def __init__(self, headers, url_prepender):
        self.headers = headers
        self.url_prepender = url_prepender

    def send_post_request_receive_json(self, method, data, header_override=None):
        return json.loads(self.send_post_request(method, data, header_override).text)

    def send_get_request_receive_json(self, method, header_override=None):
        return json.loads(self.send_get_request(method, header_override).text)

    def send_put_request_receive_json(self, method, data, header_override=None):
        return json.loads(self.send_put_request(method, data, header_override).text)

    def send_post_request(self, method, request_payload, header_override=None):
        active_headers = self.headers
        if header_override:
            active_headers = header_override

        resp = requests.post('{}{}'.format(self.url_prepender, method),
                             headers=active_headers,
                             data=request_payload)
        print('{}: {} seconds elapsed'.format(method, str(resp.elapsed.total_seconds())))
        return resp

    def send_get_request(self, method, header_override=None):
        active_headers = self.headers
        if header_override:
            active_headers = header_override

        resp = requests.get('{}{}'.format(self.url_prepender, method),
                            headers=active_headers)
        print('{}: {} seconds elapsed'.format(method, str(resp.elapsed.total_seconds())))
        return resp

    def send_put_request(self, method, request_payload, header_override=None):
        active_headers = self.headers
        if header_override:
            active_headers = header_override

        resp = requests.put('{}{}'.format(self.url_prepender, method),
                            headers=active_headers,
                            data=request_payload)
        print('{}: {} seconds elapsed'.format(method, str(resp.elapsed.total_seconds())))
        return resp

    def send_delete_request(self, method, header_override=None):
        active_headers = self.headers
        if header_override:
            active_headers = header_override

        resp = requests.delete('{}{}'.format(self.url_prepender, method),
                               headers=active_headers)
        print('{}: {} seconds elapsed'.format(method, str(resp.elapsed.total_seconds())))
        return resp
