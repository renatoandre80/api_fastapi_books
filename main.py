from fastapi import FastAPI
from app.routes.books import router as books_router

app = FastAPI()

# Registra as rotas
app.include_router(books_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de livros!"}