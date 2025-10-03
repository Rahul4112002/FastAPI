from fastapi import FastAPI, Depends

app = FastAPI()


class Settings:
    def __init__(self):
        self.api_key = 'my_secret'
        self.debug = True


def get_settings():
    return Settings()


@app.get('/config')
def get_conifig(settings: Settings = Depends(get_settings)):
    return {'api_key': settings.api_key}