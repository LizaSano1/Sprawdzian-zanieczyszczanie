import requests

class KlientAPI:
    def __init__(self, token_api):
        self.token_api = token_api

    def pobierz_dane_zanieczyszczenia_powietrza(self, miasto):
        url = f"https://api-docs.iqair.com/api/v1/{miasto}/"
        headers = {"Authorization": f"Bearer {self.token_api}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print("Błąd pobierania danych:", response.status_code)
            return None
