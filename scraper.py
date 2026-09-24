from serpapi import GoogleSearch

# Sem vložte váš API klíč ze serpapi.com
API_KEY = "fc1076ff5d9b479c2fad5d28394ce711b3b801da16d8370e1363d2fe660b10e6"

def search_google(query):
    params = {
        "engine": "google",
        "q": query,
        "hl": "cs",
        "gl": "cz",
        "api_key": API_KEY
    }

    try:
        search = GoogleSearch(params)
        results_json = search.get_dict()
        
        # Vytáhneme organické výsledky vyhledávání
        organic_results = results_json.get("organic_results", [])
        
        formatted_results = []
        for item in organic_results:
            formatted_results.append({
                "title": item.get("title", ""),
                "link": item.get("link", ""),
                "snippet": item.get("snippet", "")
            })
            
        return formatted_results

    except Exception as e:
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