import pytest
from app import app
from scraper import search_google

# --- TEST 1: Test vyhledávací logiky ---
def test_search_google_structure():
    """Testuje, zda vyhledávání přes SerpAPI vrací správný formát a strukturu dat."""
    query = "INIZIO"
    results = search_google(query)
    
    assert isinstance(results, list), "Výstupem musí být seznam"
    assert len(results) > 0, "Seznam výsledků nesmí být prázdný"
    
    first_item = results[0]
    assert "title" in first_item, "Výsledek musí obsahovat klíč 'title'"
    assert "link" in first_item, "Výsledek musí obsahovat klíč 'link'"
    assert "snippet" in first_item, "Výsledek musí obsahovat klíč 'snippet'"
    
    assert isinstance(first_item["title"], str), "Titulkový text musí být string"
    assert isinstance(first_item["link"], str), "URL odkazu musí být string"
    assert first_item["link"].startswith("http"), "Odkaz musí začínat na 'http'"


# --- TEST 2: Test Flask API rozhraní (Edge Case) ---
def test_api_empty_query_validation():
    """Testuje, zda Flask API správně zachytí a odmítne prázdný dotaz (Kód 400)."""
    # Vytvoříme testovacího klienta pro Flask server
    client = app.test_client()
    
    # Pošleme prázdný dotaz na API
    response = client.post("/api/search", json={"query": ""})
    
    # Ověříme, že server vrátí HTTP kód 400 (Bad Request)
    assert response.status_code == 400, "Server měl vrátit status code 400"
    
    # Ověříme, že odpověď obsahuje chybovou hlášku
    data = response.get_json()
    assert "error" in data, "Odpověď musí obsahovat klíč 'error'"
    assert data["error"] == "Prázdný dotaz"