from serpapi import GoogleSearch

API_KEY = "eebcfc5ba39c3d189139ea8ad9048fd274483a415e3dbe2bd7f86f072a7a2c3a"

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
