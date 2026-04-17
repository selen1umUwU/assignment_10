from flask import Flask
import json

app = Flask(__name__)

airports = {
    "LFLL": {
        "name": "Lyon Saint-Exupery Airport",
        "city": "Lyon",
        "country": "FR"
    },
    "VVTS": {
        "name": "Tan Son Nhat International Airport",
        "city": "Ho Chi Minh City",
        "country": "VN"
    },
    "VVNB": {
        "name": "Noi Bai International Airport",
        "city": "Hanoi",
        "country": "VN"
    }
}

@app.route('/airport/<icao>')
def airport_info(icao):
    icao = icao.upper()

    if icao in airports:
        response = {
            "icao": icao,
            "name": airports[icao]["name"],
            "city": airports[icao]["city"],
            "country": airports[icao]["country"]
        }
        return json.dumps(response)

    else:
        error_response = {
            "error": "Airport not found"
        }
        return json.dumps(error_response), 404


if __name__ == '__main__':
    app.run(use_reloader = True, host='127.0.0.1', port=5000)