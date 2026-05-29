import json

from flask import Flask, render_template, redirect, request, jsonify

import reqs

def load_data():
    with open("data.json", "r", encoding="utf-8") as file:
        return json.load(file)

app = Flask(__name__)

app.json.ensure_ascii = False

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html", requests=reqs.AVAILABLE_REQUESTS)

@app.route("/user_request", methods=["POST"])
def query():
    user_request = request.form.get("user_request")
    return redirect(user_request)

@app.route("/get_all_items")
def get_all_items():
    data = load_data()
    return jsonify(data)

@app.route("/get_all_<string:category>")
def get_all_films(category):
    data = load_data()

    if category in data.keys():
        return jsonify(data[category])
    else:
        return redirect(f"/get_all_{category}")

@app.route("/get_<item_category>/")
def get_item_from_category(item_category):
    CATEGORY_ASSOCIATIONS = {
        "film": "films",
        "game": "games",
        "anime": "anime",
        "series": "series",
        "book": "books"
    }
    
    data = load_data()

    id = request.args.get("id")
    name = request.args.get("name")
    
    key, value = None, None
    if id:
        key, value = "id", id
    elif name:
        key, value = "name", name

    if not key:
        return jsonify({"error": "Нет такого параметра"}), 404

    result = {}
    for item in data.get(CATEGORY_ASSOCIATIONS[item_category], []):
        if str(item.get(key)).lower() == str(value).lower():
            result = item
            break

    return jsonify(result)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("page_not_found.html"), 404

if __name__ == "__main__":
    app.run(debug=False, port=1111)