from app.services.books import search_books
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

def test_search_books():
    result = search_books("python")
    assert result.kind == "books#volumes"
    assert result.totalItems > 0
    assert len(result.items) > 0