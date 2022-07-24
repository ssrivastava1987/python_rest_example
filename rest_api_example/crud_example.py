from flask import Flask, request, jsonify

crud_example = Flask(__name__)

COUNTRIES = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]


def _find_next_id():
    return max(country["id"] for country in COUNTRIES) + 1


@crud_example.get("/countries")
def get_countries():
    return jsonify(COUNTRIES)


@crud_example.post("/countries")
def add_countries():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        COUNTRIES.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415
