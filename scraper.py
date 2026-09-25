import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

# Načte proměnné ze souboru .env
load_dotenv()

def search_google(query):
    api_key = os.environ.get("SERPAPI_KEY")
    
    if not api_key:
        print("Chyba: SERPAPI_KEY není nastaven!")
        return []

    params = {
        "q": query,
        "engine": "google",
        "api_key": api_key,
        "hl": "cs",
        "gl": "cz"
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        organic_results = results.get("organic_results", [])

        output = []
        for item in organic_results:
            output.append({
                "title": item.get("title", ""),
                "link": item.get("link", ""),
                "snippet": item.get("snippet", "")
            })
        return output
    except Exception as e:
        print(f"Chyba při vyhledávání: {e}")
        return []