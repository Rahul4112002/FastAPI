from fastapi import FastAPI
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware

app = FastAPI()

app.add_middleware(
    HTTPSRedirectMiddleware
)