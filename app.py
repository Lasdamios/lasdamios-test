from flask import Flask, render_template, request, jsonify
from scraper import search_google

app = Flask(__name__)

@app.route("/")
def home():
    # Načte HTML rozhraní
    return render_template("index.html")

@app.route("/api/search", methods=["POST"])
def api_search():
    # Přijme klíčové slovo z frontendu a vrátí nalezené výsledky
    data = request.get_json()
    query = data.get("query", "").strip()
    
    if not query:
        return jsonify({"error": "Prázdný dotaz"}), 400
        
    results = search_google(query)
    return jsonify({"results": results})

if __name__ == "__main__":
    app.run(debug=True, port=5000)