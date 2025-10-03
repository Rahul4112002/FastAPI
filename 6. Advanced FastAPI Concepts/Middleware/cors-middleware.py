from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    allow_origins = ['http//:my-frontend.com', 'http//:localhost:3000'],
    allow_credentials = True,
    allow_methods = ['GET','POST','PUT','DELETE'],
    allow_headers = ['*']
)