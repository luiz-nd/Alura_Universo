# 📖 Alura Album - Copa do Mundo Tech

Este projeto é um **Álbum de Figurinhas Virtual Interativo** desenvolvido durante a Imersão Alura. O projeto apresenta figuras ilustres ("Tech Legends") da área de tecnologia organizadas por categorias, oferecendo uma experiência imersiva de folhear páginas com efeitos visuais modernos e sonorização dinâmica.

---

## 🎯 Objetivo do Projeto

O objetivo principal é criar um álbum de figurinhas virtual interativo que consome dados de uma API (FastAPI) para preencher dinamicamente as figurinhas colecionáveis dos pioneiros e celebridades da tecnologia (Inteligência Artificial, Python, Banco de Dados, Sistemas Operacionais e Celebridades Tech do Brasil). 

A aplicação foca em uma experiência de usuário (UX) rica, com folheamento de páginas fluido em 3D, efeitos sonoros sintetizados em tempo real e visual moderno com temática futurista.

---

## 📂 Funcionalidade dos Arquivos Envolvidos

O projeto é composto por três arquivos principais na raiz, cada um responsável por uma camada da aplicação (estrutura, estilo e comportamento):

### 1. 📄 [index.html](file:///c:/Users/nxznt/Desktop/luiz%20felipe%20bacupe/Backup%20novo%20pc/ADS/Alura_Aulas/i-arq-ia-alura-album-main/index.html)
Define a estrutura semântica do álbum de figurinhas.
- **Capa do Livro (Página 0):** Contém elementos gráficos futuristas (efeito *glitch*, mini cards flutuantes e uma esfera tecnológica em 3D).
- **Páginas Temáticas:** Estruturadas com grids contendo slots numerados para cada figurinha, categorizados em:
  - **IA:** Pioneiros da Inteligência Artificial.
  - **Python:** Arquitetos da Simplicidade.
  - **Banco de Dados:** Arquitetos de Bancos de Dados.
  - **Sistemas Operacionais:** Criadores da Computação Moderna.
  - **Brasil (Vol. 1 e 2):** Celebridades e educadores tech do cenário nacional.
- **Controles de UI:** Botões de navegação lateral (próximo/anterior) e controle de áudio (mutar/desmutar).

### 2. 🎨 [style.css](file:///c:/Users/nxznt/Desktop/luiz%20felipe%20bacupe/Backup%20novo%20pc/ADS/Alura_Aulas/i-arq-ia-alura-album-main/style.css)
Responsável por toda a identidade visual, design responsivo e efeitos estéticos da aplicação.
- **Design System:** Definição de paleta de cores futurista (tons de azul cósmico, azul escuro, preto profundo e detalhes neon), tipografia moderna (fontes *Inter* e *Outfit*) e variáveis CSS.
- **Efeitos Tridimensionais e Sombras:** Sombras dinâmicas e gradientes que simulam a lombada e as dobras das páginas de um livro real.
- **Micro-animações:** Efeito de *glitch* nos títulos, animação de levitação/flutuação dos mini cards na capa, rotação de anéis na esfera tecnológica central e transições suaves nos slots e botões.
- **Estados Visuais:** Estilos para os slots de figurinhas vazios (com bordas tracejadas) e preenchidos (com transição suave de revelação das imagens).

### 3. ⚙️ [app.js](file:///c:/Users/nxznt/Desktop/luiz%20felipe%20bacupe/Backup%20novo%20pc/ADS/Alura_Aulas/i-arq-ia-alura-album-main/app.js)
Controla a lógica da aplicação, a interatividade do álbum e a integração com o servidor.
- **Integração com API (Backend):** A função assíncrona `preencherFigurinhas()` faz uma requisição `GET` para a rota `/figurinhas` da API local (por padrão em `http://localhost:8000`), mapeia as imagens retornadas e insere-as dinamicamente nos slots correspondentes.
- **Biblioteca St.PageFlip:** Inicializa e configura o motor de simulação física do livro de páginas folheáveis com suporte a arraste via mouse/touch e responsividade adaptativa.
- **Sintetizador de Áudio (Web Audio API):** Gera dinamicamente o som físico de papel amassado/virando através de síntese de ruído branco com filtros passa-faixa (*bandpass*) e passa-baixa (*lowpass*), eliminando a necessidade de arquivos de áudio externos estáticos.
- **Controles e Navegação:** Escuta cliques nos botões da tela e teclas direcionais do teclado (`ArrowLeft` / `ArrowRight`) para folhear o álbum, além de gerenciar o estado mutado/ativo do áudio.

---

## 🛠️ Como Executar o Projeto

1. **Requisito do Backend:** Certifique-se de que a API de figurinhas está rodando. O endpoint padrão esperado é `http://localhost:8000/figurinhas`.
   - Para iniciar o servidor FastAPI (conforme instruções no arquivo):
     ```bash
     cd backend/dia-3
     uvicorn main:app --reload
     ```
2. **Executar o Frontend:** Abra o arquivo [index.html](file:///c:/Users/nxznt/Desktop/luiz%20felipe%20bacupe/Backup%20novo%20pc/ADS/Alura_Aulas/i-arq-ia-alura-album-main/index.html) em um navegador web ou utilize um servidor local de desenvolvimento (como a extensão Live Server do VS Code).
