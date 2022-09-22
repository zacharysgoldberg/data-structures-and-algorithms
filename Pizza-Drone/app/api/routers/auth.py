from typing import Optional
from fastapi import APIRouter, Depends, Request, Response, HTTPException
from ..models import Users, Base
from passlib.context import CryptContext
from ..database import SessionLocal, engine, db
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

# [Authorization and authentication]

SECRET_KEY = '3K75JD2JKDS99U342YINQ0'

ALGORITHM = "HS256"

by_crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={401: {"user": "Not authorized"}}
)

Base.metadata.create_all(bind=engine)

oatuh2_bearer = OAuth2PasswordBearer(tokenUrl='token')


def hash_password(password):
    return by_crypt_context.hash(password)


def verfiy_password(password, hashed_password):
    return by_crypt_context.verify(password, hashed_password)


def authenticate_user(username: str, password: str, db: Session = Depends(db)):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False

    if not verfiy_password(password, user.password):
        return False

    return user

# [Creating access token]


def create_access_token(username: str,
                        user_id: int,
                        expires_delta: Optional[timedelta] = None):
    encode = {"sub": username, "id": user_id}
    if expires_delta:
        expire = datetime.utcnow() + expires_delta

    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    encode.update({"exp": expire})
    # [Encoding JWT]
    encoded_jwt = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# [Check is current user has a valid access token]


async def get_current_user(request: Request):
    try:
        token = request.cookies.get('access_token')
        if token is None:
            return None
        # [Decoding JWT]
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if username is None or user_id is None:
            return False

        return {"username": username, "id": user_id}

    except JWTError:
        return HTTPException(status_code=404, detail="Not found")

# [Login logic for setting access token as cookie]


@router.post('/token')
async def login_for_access_token(response: Response,
                                 form_data: OAuth2PasswordRequestForm = Depends(),
                                 db: Session = Depends(db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # [Setting token expiration to 1 hour]
    token_expires = timedelta(minutes=60)
    access_token = create_access_token(user.username,
                                       user.id,
                                       expires_delta=token_expires)
    # [Setting JWT as cookie]
    response.set_cookie(key="access_token", value=access_token, httponly=True)

    return True
