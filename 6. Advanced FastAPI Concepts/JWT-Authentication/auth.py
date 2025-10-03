from datetime import datetime, timedelta, timezone
from authlib.jose import JoseError, jwt
from fastapi import HTTPException

# constants
SECRET_KEY = 'my_secret'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRY_MINUTES = 30


# functions
def create_access_token(data: dict):
    header = {'alg': ALGORITHM}
    expire = datetime.now(timezone.utc) + timedelta(ACCESS_TOKEN_EXPIRY_MINUTES)
    payload = data.copy()
    payload.update({'exp': expire})
    return jwt.encode(header, payload, SECRET_KEY).decode('utf-8')


def verify_token(token: str):
    try:
        claims = jwt.decode(token, SECRET_KEY)
        claims.validate()
        username = claims.get('sub')
        if username is None:
            raise HTTPException(status_code=401, detail='Token missing')
        return username
    except JoseError:
        raise HTTPException(status_code=401, detail="Couldn't Validate Credentials")