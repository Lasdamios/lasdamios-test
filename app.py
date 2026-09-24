import os
from flask import Flask, render_template, request, jsonify
from scraper import search_google

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/search", methods=["POST"])
def api_search():
    data = request.get_json()
    query = data.get("query", "").strip()
    
    if not query:
        return jsonify({"error": "Prázdný dotaz"}), 400
        
    results = search_google(query)
    return jsonify({"results": results})

if __name__ == "__main__":
    # Render automaticky předává port v proměnné prostředí PORT (případně použije 5000 pro lokální vývoj)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)