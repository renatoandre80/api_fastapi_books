from fastapi import APIRouter, HTTPException
import requests
from app.schemas.books import GoogleBooksResponse, Volume
from app.services.books import search_books

router = APIRouter()

@router.get("/books", response_model=GoogleBooksResponse)
def get_books(query: str):
    try:
        return search_books(query)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/books")
def add_book(book: Volume):
    # Aqui você pode adicionar lógica para salvar o livro em um banco de dados.
    return {"message": "Livro adicionado com sucesso!", "book": book}