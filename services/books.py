import requests
from app.schemas.books import GoogleBooksResponse

def search_books(query: str) -> GoogleBooksResponse:
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {"q": query}
    response = requests.get(url, params=params)
    return GoogleBooksResponse(**response.json())