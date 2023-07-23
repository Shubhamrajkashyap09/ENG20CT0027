from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def fetch_numbers_from_url(url):
    try:
        response = requests.get(url)
        data = response.json()
        return data.get("numbers", [])
    except Exception as e:
        print(f"Error fetching numbers from {url}: {e}")
        return []

@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')

    if not urls:
        return jsonify({"error": "No URLs provided"}), 400

    result = {}
    for url in urls:
        numbers = fetch_numbers_from_url(url)
        result[url] = numbers

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)