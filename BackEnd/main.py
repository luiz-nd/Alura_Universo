from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import glob

# Inicializa a aplicação FastAPI
app = FastAPI()

# Configure o middleware CORS para aceitar requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Defina caminhos absolutos para a pasta de imagens usando:
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Lista de figurinhas com as 30 figurinhas, com as não disponíveis comentadas
figurinhas = [
    {
        "id": 1,
        "nome": "Mercúrio",
        "categoria": "Sistema Solar Interno",
        "imagem_url": "/figurinhas/1/imagem"
    },
    {
        "id": 2,
        "nome": "Vênus",
        "categoria": "Sistema Solar Interno",
        "imagem_url": "/figurinhas/2/imagem"
    },
    {
         "id": 3,
         "nome": "Terra",
        "categoria": "Sistema Solar Interno",
        "imagem_url": "/figurinhas/3/imagem"
     },
     {
         "id": 4,
         "nome": "Marte",
         "categoria": "Sistema Solar Interno",
        "imagem_url": "/figurinhas/4/imagem"
     },
     {
         "id": 5,
         "nome": "Sol",
         "categoria": "Sistema Solar Interno",
         "imagem_url": "/figurinhas/5/imagem"
     },
     {
         "id": 6,
         "nome": "Júpiter",
         "categoria": "Sistema Solar Externo",
         "imagem_url": "/figurinhas/6/imagem"
     },
    {
        "id": 7,
        "nome": "Saturno",
        "categoria": "Sistema Solar Externo",
        "imagem_url": "/figurinhas/7/imagem"
    },
    {
        "id": 8,
        "nome": "Urano",
        "categoria": "Sistema Solar Externo",
        "imagem_url": "/figurinhas/8/imagem"
    },
    {
        "id": 9,
        "nome": "Netuno",
        "categoria": "Sistema Solar Externo",
        "imagem_url": "/figurinhas/9/imagem"
    },
     {
         "id": 10,
         "nome": "Plutão",
         "categoria": "Sistema Solar Externo",
         "imagem_url": "/figurinhas/10/imagem"
     },
     {
         "id": 11,
         "nome": "Nebulosa de Órion",
         "categoria": "Estrelas e Nebulosas",
         "imagem_url": "/figurinhas/11/imagem"
     },
     {
         "id": 12,
         "nome": "Nebulosa da Hélice",
         "categoria": "Estrelas e Nebulosas",
         "imagem_url": "/figurinhas/12/imagem"
     },
     {
         "id": 13,
         "nome": "Sirius",
         "categoria": "Estrelas e Nebulosas",
         "imagem_url": "/figurinhas/13/imagem"
     },
    {
        "id": 14,
        "nome": "Betelgeuse",
        "categoria": "Estrelas e Nebulosas",
        "imagem_url": "/figurinhas/14/imagem"
    },
     {
         "id": 15,
         "nome": "Próxima Centauri",
         "categoria": "Estrelas e Nebulosas",
         "imagem_url": "/figurinhas/15/imagem"
     },
     {
         "id": 16,
         "nome": "Via Láctea",
         "categoria": "Galáxias do Universo",
         "imagem_url": "/figurinhas/16/imagem"
     },
     {
         "id": 17,
         "nome": "Andrômeda",
         "categoria": "Galáxias do Universo",
         "imagem_url": "/figurinhas/17/imagem"
     },
     {
         "id": 18,
         "nome": "Galáxia do Sombrero",
         "categoria": "Galáxias do Universo",
         "imagem_url": "/figurinhas/18/imagem"
     },
     {
         "id": 19,
         "nome": "Galáxia do Triângulo",
         "categoria": "Galáxias do Universo",
         "imagem_url": "/figurinhas/19/imagem"
     },
     {
         "id": 20,
         "nome": "Nuvem de Magalhães",
         "categoria": "Galáxias do Universo",
         "imagem_url": "/figurinhas/20/imagem"
     },
    {
         "id": 21,
         "nome": "Sagitário A ",
         "categoria": "Mistérios e Fenômenos Cósmicos",
         "imagem_url": "/figurinhas/21/imagem"
     },
     {
         "id": 22,
         "nome": "Quasar",
         "categoria": "Mistérios e Fenômenos Cósmicos",
         "imagem_url": "/figurinhas/22/imagem"
     },
    {
         "id": 23,
         "nome": "Estrela de Nêutrons",
         "categoria": "Mistérios e Fenômenos Cósmicos",
         "imagem_url": "/figurinhas/23/imagem"
     },
    {
         "id": 24,
         "nome": "Supernova",
         "categoria": "Mistérios e Fenômenos Cósmicos",
         "imagem_url": "/figurinhas/24/imagem"
     },
    {
         "id": 25,
         "nome": "Matéria Escura",
         "categoria": "Mistérios e Fenômenos Cósmicos",
         "imagem_url": "/figurinhas/25/imagem"
     },
    {
         "id": 26,
         "nome": "Telescópio James Webb",
         "categoria": "Exploração do Espaço",
         "imagem_url": "/figurinhas/26/imagem"
     },
    {
         "id": 27,
         "nome": "Telescópio Hubble",
         "categoria": "Exploração do Espaço",
         "imagem_url": "/figurinhas/27/imagem"
     },
    {
         "id": 28,
         "nome": "Sonda Voyager 1",
         "categoria": "Exploração do Espaço",
         "imagem_url": "/figurinhas/28/imagem"
     },
    {
         "id": 29,
         "nome": "Rover Curiosity",
         "categoria": "Exploração do Espaço",
         "imagem_url": "/figurinhas/29/imagem"
     },
    #{
    #    "id": 30,
    #    "nome": "Você no Espaço",
    #    "categoria": "Exploração do Espaço",
    #    "imagem_url": "/figurinhas/30/imagem"
    #}
]

# Endpoint GET "/figuras" que retorna a lista
# Também mapeamos "/figurinhas" para compatibilidade com o frontend
@app.get("/figuras")
@app.get("/figurinhas")
def listar_figurinhas():
    return figurinhas

# Endpoint GET "/figurinhas/{id}/imagem"
@app.get("/figurinhas/{id}/imagem")
def obter_imagem(id: int):
    # Use glob para encontrar o arquivo com prefixo "{id:02d}[!0-9]*" na pasta figurinhas/
    busca_padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    arquivos = glob.glob(busca_padrao)
    
    # Retornar 404 se não encontrar
    if not arquivos:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")
    
    # Retorna FileResponse com o arquivo encontrado
    return FileResponse(arquivos[0])
