from flask import Flask, request, jsonify
from flask_cors import CORS
from link_factory import save_new_links

app = Flask(__name__)
CORS(app)

def save_new_links(link, filename):
    try:
        with open(filename, 'a') as file:
            file.write(link)
    except Exception as e:
        raise Exception(f"Error saving link: {str(e)}")

@app.route('/save-link-banner', methods=['POST'])
def save_link_banner():
    try:
        data = request.get_json()
        link = data.get('link')
        if link:
            save_new_links(link + '\n', 'linksBanner.txt')
            return jsonify({"message": "Link saved successfully"}), 200
        return jsonify({"message": "Invalid input"}), 400
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

@app.route('/save-link-most', methods=['POST'])
def save_link_most():
    try:
        data = request.get_json()
        link = data.get('link')
        if link:
            save_new_links(link + '\n', 'linksMost.txt')
            return jsonify({"message": "Link saved successfully"}), 200
        return jsonify({"message": "Invalid input"}), 400
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

@app.route('/save-link-trending', methods=['POST'])
def save_link_trending():
    try:
        data = request.get_json()
        link = data.get('link')
        if link:
            save_new_links(link + '\n', 'linksTrending.txt')
            return jsonify({"message": "Link saved successfully"}), 200
        return jsonify({"message": "Invalid input"}), 400
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
