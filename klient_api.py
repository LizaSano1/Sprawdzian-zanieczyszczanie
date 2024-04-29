import requests

class KlientAPISerwisuJakościPowietrza:
    def __init__(self, token_api):
        self.token_api = token_api
        self.bazowy_adres_url = "https://api-docs.iqair.com"

    def pobierz_dane_jakości_powietrza(self, miasto):
        nagłówki = {"Authorization": f"Bearer {self.token_api}"}
        parametry = {"city": miasto}
        odpowiedź = requests.get(f"{self.bazowy_adres_url}/data", headers=nagłówki, params=parametry)
        if odpowiedź.status_code == 200:
            return odpowiedź.json()
        else:
            return None
