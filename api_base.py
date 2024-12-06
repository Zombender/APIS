import requests
from requests.exceptions import RequestException

class APIBase():
    def __init__(self,base_url:str):
        self.base_url = base_url
    
    def post_response(self,data,headers,url=None)->None|requests.Response:
        url = url or self.base_url
        try:
            response:requests.Response = requests.post(url,json=data,headers=headers)
            if not response.ok:
                raise RequestException
        except RequestException:
            print(f"Error en la respuesta HTTP: {response} --- {response.status_code} --- {response.text}")
            return None
        return response
    
    def get_response(self,headers=None,url=None)->None | requests.Response:
        url = url or self.base_url
        try:
            response:requests.Response = requests.get(url,headers=headers)
            if response.text == '': raise RequestException
        except RequestException:
            print(f"Error en la respuesta HTTP: {response} --- Codigo: {response.status_code} --- Contenido: {response.text}")
            return None
        
        return response
    
