from flask import Flask, request, jsonify
from datetime import datetime
from pydantic import BaseModel, ValidationError, validator

app = Flask(__name__)

class WeatherData(BaseModel):
    timestamp: datetime
    temperature: float
    pressure: int

    @validator("temperature")
    def validate_temperature(cls, value):
        if value < -50 or value > 50:
            raise ValueError("Temperature must be between -50°C and 50°C")
        return value

    @validator("pressure")
    def validate_pressure(cls, value):
        if value < 800 or value > 1200:
            raise ValueError("Pressure must be between 800 hPa and 1200 hPa")
        return value

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

weather_service = WeatherService()

@app.route("/weather", methods=["POST"])
def add_weather():
    data = request.json
    try:
        weather_data = WeatherData(**data)
        weather_service.add_weather_data(weather_data.dict())
        return jsonify({"message": "Weather data added successfully"}), 201
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400

@app.route("/weather", methods=["GET"])
def get_closest_weather():
    timestamp_str = request.args.get("timestamp")
    if not timestamp_str:
        return jsonify({"error": "Timestamp parameter is required"}), 400

    try:
        timestamp = datetime.fromisoformat(timestamp_str)
    except ValueError:
        return jsonify({"error": "Invalid timestamp format. Please use ISO 8601 format"}), 400

    closest_weather_data = weather_service.get_closest_weather_data(timestamp)

    if closest_weather_data:
        return jsonify(closest_weather_data)
    else:
        return jsonify({"error": "No available weather data"}), 404

if __name__ == "__main__":
    app.run(debug=True)
