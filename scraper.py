import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

<<<<<<< HEAD
# Načte proměnné ze souboru .env
load_dotenv()
=======
API_KEY = "eebcfc5ba39c3d189139ea8ad9048fd274483a415e3dbe2bd7f86f072a7a2c3a"
>>>>>>> dfbd9d684d8a1e2483cac91887070360202973b4

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
<<<<<<< HEAD
        print(f"Chyba při vyhledávání: {e}")
        return []
=======
        print(f"Chyba při komunikaci s API: {e}")
        return []

if __name__ == "__main__":
    test_query = "INIZIO Internet Media"
    print(f"Vyhledávám přes SerpAPI: '{test_query}'...\n")
    data = search_google(test_query)
    
    if not data:
        print("Nenalezeny žádné výsledky nebo chybí API klíč.")
    else:
        for idx, item in enumerate(data, 1):
            print(f"{idx}. {item['title']}")
            print(f"   URL: {item['link']}")
            print(f"   Popis: {item['snippet'][:100]}...")
            print("-" * 40)
>>>>>>> dfbd9d684d8a1e2483cac91887070360202973b4
