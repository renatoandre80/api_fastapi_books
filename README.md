

# A arquitetura desse projeto segue o livro cosmic python, separando os dominios de negocios e utilizando testes

# Utilizando fastapi, pydantic para os schemas e validação de dados e pytest para o teste unitário.

# Teste unitário

# para rodar o teste unitário no lugar de aplicar o pytest na pasta app ou dentro de test utilizar o comando abaixo na raíz:
PYTHONPATH=. pytest

# Para rodar no terminal digite: fastapi dev main dentro de app

# exemplo de teste com query parameters retorna todos os livros de física na api do google:

http://127.0.0.1:8000/books?query=fisica

# Acessando a doc swagger:

http://127.0.0.1:8000/docs

segue a imagem da doc onde é possível enviar um get e um post , métodos http

![Doc FastAPI](app\doc_fastapi.png)