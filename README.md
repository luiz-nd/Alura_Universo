# Alura_Universo
# 🌌 Alura Universo — Álbum de Figurinhas Espacial

> 🚀 **Alura_Universo** é uma aplicação web interativa desenvolvida em HTML, CSS, JavaScript e FastAPI (Python) para gerenciamento e visualização de um álbum de figurinhas astronômico do Sistema Solar.
>
> O projeto conta com rotas dinâmicas para entrega de imagens, suporte a fotos personalizadas do usuário e interface interativa com suporte a animações e efeitos no *hover*.

---

## ✨ Destaques do Projeto

* 🪐 **Álbum do Sistema Solar:** Figurinhas interativas de planetas e corpos celestes com informações detalhadas e efeito visual no *hover* (escurecimento e destaque do slot).
* ⚡ **API FastAPI:** Servidor backend com CORS totalmente habilitado e gerenciamento dinâmico de arquivos de imagem via endpoint (`/figurinhas/{id}/imagem`).
* 📸 **Figurinha Personalizada (#30):** Tratamento dinâmico para o slot do usuário, pronto para receber uploads.
* 🛠️ **Arquitetura Sólida:** Mapeamento automático por `glob` e tratamento de erros (HTTP 404) para imagens não encontradas.

---

## 💻 Tech Stack

| Camada | Tecnologia |
| :--- | :--- |
| **Frontend** | HTML5, CSS3, JavaScript (ES6+) |
| **Backend** | Python 3, FastAPI, Uvicorn |
| **Integrações** | CORS Middleware, REST API, FileResponse |

---

## 📂 Estrutura de Pastas

```text
Alura_Universo/
├── figurinhas/         # Pasta contendo as imagens das figurinhas (01-Mercúrio, 02-Vênus, ...)
├── main.py             # Servidor principal da API FastAPI
├── index.html          # Interface do álbum de figurinhas
├── style.css           # Estilização com animações e efeitos de hover
├── script.js          # Consumo da API e renderização dos cards
└── README.md           # Documentação do projeto
