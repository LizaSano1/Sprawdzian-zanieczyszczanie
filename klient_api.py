import requests

class AirQualityAPIClient:
    def __init__(self, api_token):
        self.api_token = api_token
        self.base_url = "https://api-docs.iqair.com"

    def get_air_quality_data(self, city):
        headers = {"Authorization": f"Bearer {self.api_token}"}
        params = {"city": city}
        response = requests.get(f"{self.base_url}/data", headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None
