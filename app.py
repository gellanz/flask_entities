from flask import Flask, jsonify, request
from named_entities import SpanishNER

app = Flask(__name__)


@app.route("/api/ner", methods=["POST"])
def process_named_entities():
    data = request.json  # Get the JSON data from the request
    sentences = data["sentences"]
    results = []
    model_ner = SpanishNER()
    for sentence in sentences:
        results.append(model_ner.get_ner(sentence))

    response_data = {"message": "Data received successfully", "results": results}

    return jsonify(response_data), 201


if __name__ == "__main__":
    app.run(debug=True)
