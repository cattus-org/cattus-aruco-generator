# ArUco Generator API

API FastAPI para gerar etiquetas ArUco personalizáveis e retornar as imagens em base64.

## Descrição

Esta API permite gerar etiquetas ArUco via HTTP, útil para aplicações que precisam de marcadores visuais para visão computacional.

## Endpoints

- `GET /generate`: Gera um marcador ArUco com os parâmetros passados via query string.
  - Parâmetros:
    - `id` (int, obrigatório): ID do marcador ArUco (0-1023).
    - `size` (int, opcional, padrão=200): Tamanho do marcador em pixels (50-1000).
    - `margin_size` (int, opcional, padrão=10): Margem ao redor do marcador (0-100).
    - `border_bits` (int, opcional, padrão=1): Bits da borda do marcador (1-4).
  - Retorna: JSON com o ID e a imagem do marcador em base64.

- `GET /generate_row`: Gera uma linha de marcadores ArUco com os parâmetros passados via query string.
  - Parâmetros:
    - `id` (int, obrigatório): ID do marcador ArUco (0-1023).
    - `count` (int, opcional, padrão=10): Número de marcadores na linha (2-10).
    - `size` (int, opcional, padrão=35): Tamanho do marcador em pixels (10-100).
    - `margin_size` (int, opcional, padrão=10): Margem ao redor do marcador (0-100).
    - `border_bits` (int, opcional, padrão=1): Bits da borda do marcador (1-4).
  - Retorna: JSON com o ID, a contagem e a imagem da linha de marcadores em base64.

- `GET /health`: Endpoint para checagem de saúde da API.

- `GET /docs`: Endpoint para a documentação interativa da API gerada pelo Swagger UI.

- `GET /`: Endpoint raiz com mensagem de boas-vindas.

## Como rodar localmente

1. Clone o repositório
2. Crie e ative um ambiente virtual
3. Instale as dependências com `pip install -r requirements.txt`
4. Execute a aplicação com `uvicorn lambda_function:app --reload`

## Observações

- Os IDs dos marcadores para a rota `/generate` são de 0 a 1023.
- Para a rota `/generate_row`, os IDs podem variar de 0 a 1023, e o número de marcadores na linha pode ser de 2 a 10.
- Os tamanhos e margens possuem limites para evitar erros na geração das imagens.