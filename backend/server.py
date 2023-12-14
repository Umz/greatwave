import requests
from flask import Flask, jsonify, Response, request
from flask_cors import CORS
from dataFormat import getData

app = Flask(__name__)
CORS(app)

# Load all locations from the spreadsheet and get lon, lat

locations = {
    "London": {"longitude": -0.1274, "latitude": 51.50853},
    "New York": {"longitude": -74.00597, "latitude": 40.71427},
    "Tokyo": {"longitude": 139.69171, "latitude": 35.6895},
}

@app.route('/', methods=['GET'])
def hello():

    key = '#'
    city = request.args.get('city', default='London', type=str)
    lon, lat = locations[city]["longitude"], locations[city]["latitude"]
    
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}'

    response = requests.get(url)
    if response.status_code == 200:
        json = response.json()
        data = getData(json)
        return jsonify(data)
    else:
        return Response("{'a':'b'}", status=500, mimetype='application/json')
    
if (__name__ == '__main__'):
    app.run(debug=True)