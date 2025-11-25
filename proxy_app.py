# proxy_app.py
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import httpx
import os

app = FastAPI()

# URLs dos seus apps
FRONTEND_URL = "https://sexto-andar-web-9a6357fcb391.herokuapp.com"
AUTH_URL = "https://sexto-andar-auth-6def0cff0560.herokuapp.com"
API_URL = "https://sexto-andar-api-3ef30ad16a1f.herokuapp.com"

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_root(path: str, request: Request):
    """Proxeia tudo do frontend"""
    if path.startswith("auth/"):
        target = f"{AUTH_URL}/{path[5:]}"
    elif path.startswith("api/"):
        target = f"{API_URL}/{path[4:]}"
    else:
        target = f"{FRONTEND_URL}/{path}"
    
    async with httpx.AsyncClient() as client:
        # Copia os headers originais
        headers = dict(request.headers)
        headers.pop("host", None)  # Remove host header
        
        # Faz a requisição pro app de destino
        response = await client.request(
            method=request.method,
            url=target,
            headers=headers,
            content=await request.body(),
            params=request.query_params,
        )
        
        # Retorna a resposta
        return StreamingResponse(
            content=response.iter_bytes(),
            status_code=response.status_code,
            headers=dict(response.headers)
        )

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
