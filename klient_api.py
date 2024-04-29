import requests

class AirQualityClient:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://api.airvisual.com/v2"

    def get_air_quality_data(self, city):
        endpoint = f"{self.base_url}/city?city={city}&state=Warsaw&country=Poland&key={self.token}"
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            return None
