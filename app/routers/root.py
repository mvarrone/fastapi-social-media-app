from datetime import datetime

from fastapi import APIRouter, Request

router = APIRouter(
    tags=["Root"]
)


@router.get("/")
async def root_endpoint(request: Request):
    # scope = request.scope
    # print(scope)

    return {
        'message': 'App is up and running',
        'time': datetime.now(),
        'http_version': request.scope.get("http_version"),
        'url': request.url,
        'url_str': str(request.url),
        'server_method': request.method,
        'server_hostname': request.url.hostname,
        'server_port': request.url.port,
        'server_is_secure': request.url.is_secure,
        'server_path': request.url.path,
        'server_scheme': request.url.scheme,
        'client_host': request.client.host,
        'client_port': request.client.port
    }
