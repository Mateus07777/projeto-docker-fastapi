# Projeto Docker - API FastAPI com PostgreSQL

## 📌 Descrição

Este projeto consiste em uma API desenvolvida com FastAPI, containerizada com Docker e utilizando PostgreSQL como banco de dados.

A aplicação realiza operações de CRUD (Create, Read e Delete), com persistência de dados através de volume Docker e comunicação entre containers por rede.

---

## 🚀 Tecnologias utilizadas

- Python (FastAPI)
- Docker
- Docker Compose
- PostgreSQL

---

## ▶️ Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU-USUARIO/projeto-docker-fastapi.git
2. Acessar a pasta
cd projeto-docker-fastapi
3. Subir os containers
docker-compose up --build -d
🌐 Acessar a API

Abra no navegador:

http://localhost:8000/docs
🛢️ Banco de dados
Host: localhost
Porta: 5433
Database: dimdim
Usuário: user
Senha: password
📂 Estrutura do projeto
projeto-docker/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── crud.py
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
👨‍💻 Autor
Mateus Teni Pierro
RM: 555125

---

# ⚠️ IMPORTANTE

👉 Troca isso aqui:
```text
SEU-USUARIO