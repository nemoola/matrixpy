import requests

class ODPT:
    def __init__(self, key):
        self.endpoint = "https://api.odpt.org/api/v4"
        self.key = key

    def get(self):
        url = f"{self.endpoint}/odpt:Station?dc:title=我孫子&acl:consumerKey={self.key}"
        print(requests.get(url).text)


odpt = ODPT("oqlnaxj5rvn7w9oc130x3tac69shqmdatdz6a5uwdme0l41jff1xx05gq11r9ids")
odpt.get()