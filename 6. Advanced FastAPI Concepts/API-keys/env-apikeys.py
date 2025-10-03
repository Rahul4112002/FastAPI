from fastapi import FastAPI, Depends, Header, HTTPException
from pydantic_settings import BaseSettings


class Setttings(BaseSettings):
    api_key: str


    class Config:
        env_file = '.env'


settings = Setttings()
app = FastAPI()


def get_api_key(api_key: str = Header(...)):
    if api_key != settings.api_key:
        raise HTTPException(status_code=403, detail='Unauthorized')
    return api_key


@app.get('/get-data')
def get_data(api_key: str = Depends(get_api_key)):
    return {'output': 'Access granted!'}