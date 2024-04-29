class WeatherService:
    def __init__(self):
        self.weather_data = []

    def add_weather_data(self, data):
        self.weather_data.append(data)

    def get_closest_weather_data(self, timestamp):
        closest_data = None
        min_difference = float("inf")
        for data in self.weather_data:
            data_timestamp = data["timestamp"]
            time_difference = abs((data_timestamp - timestamp).total_seconds())
            if time_difference < min_difference:
                closest_data = data
                min_difference = time_difference
        return closest_data