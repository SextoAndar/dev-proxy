# Sexto Andar Nginx Proxy

## Objetivo

Este serviço atua como um reverse proxy para unificar o acesso ao frontend e às APIs sob um único domínio (`localhost:8000`), resolvendo problemas de CORS e de compartilhamento de cookies de autenticação entre os diferentes serviços.

## Como Rodar

### Usando Docker

1.  **Construa a imagem Docker:**

    ```bash
    docker build -t sexto-andar-nginx .
    ```

2.  **Execute o container:**

    Para que o Nginx consiga se comunicar com os outros serviços (frontend, api, auth) que estão rodando localmente fora de containers, use a network do host.

    ```bash
    docker run --network=host -p 8000:8000 sexto-andar-nginx
    ```
    *Obs: a porta do `listen` no `nginx.conf` deve ser a mesma porta exposta.*

### Integração com Docker Compose

Se todos os serviços (frontend, api, auth) estiverem sendo orquestrados com `docker-compose` em uma mesma rede, o Nginx poderá resolvê-los pelos nomes dos serviços (`frontend`, `api`, `auth`).

Garanta que:
1.  Todos os containers estejam na mesma `network`.
2.  Os nomes dos serviços no `nginx.conf` (`frontend`, `api`, `auth`) sejam os mesmos definidos no `docker-compose.yml` de cada serviço.

Após rodar o proxy, acesse a aplicação em `http://localhost:8000`.

## Rotas

-   `http://localhost:8000/` -> Redireciona para o **frontend** (`http://frontend:3000/`)
-   `http://localhost:8000/api/` -> Redireciona para a **API de imóveis** (`http://api:8000/api/`)
-   `http://localhost:8000/auth/` -> Redireciona para a **API de autenticação** (`http://auth:8001/auth/`)
