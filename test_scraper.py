import pytest
from scraper import search_google

def test_search_google_structure():
    """Testuje, zda vyhledávání vrací správný formát a strukturu dat."""
    query = "INIZIO"
    results = search_google(query)
    
    # 1. Výstup musí být seznam (list)
    assert isinstance(results, list), "Výstupem musí být seznam"
    
    # 2. Musíme dostat alespoň jeden výsledek
    assert len(results) > 0, "Seznam výsledků nesmí být prázdný"
    
    # 3. Zkontrolujeme strukturu prvního výsledku
    first_item = results[0]
    
    assert "title" in first_item, "Výsledek musí obsahovat klíč 'title'"
    assert "link" in first_item, "Výsledek musí obsahovat klíč 'link'"
    assert "snippet" in first_item, "Výsledek musí obsahovat klíč 'snippet'"
    
    # 4. Ověříme datové typy a že URL je platná
    assert isinstance(first_item["title"], str), "Titulkový text musí být string"
    assert isinstance(first_item["link"], str), "URL odkazu musí být string"
    assert first_item["link"].startswith("http"), "Odkaz musí začínat na 'http'"