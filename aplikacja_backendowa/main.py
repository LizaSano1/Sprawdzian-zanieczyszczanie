from flask import Flask, request, jsonify
from datetime import datetime
from models import WeatherData
from services import WeatherService
from validators import handle_validation_error
from pydantic import ValidationError

app = Flask(__name__)
weather_service = WeatherService()

@app.route("/weather", methods=["POST"])
def add_weather():
    data = request.json
    try:
        weather_data = WeatherData(**data)
        weather_service.add_weather_data(weather_data.dict())
        return jsonify({"message": "Weather data added successfully"}), 201
    except ValidationError as e:
        return handle_validation_error(e)

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
