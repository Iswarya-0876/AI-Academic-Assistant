from jose import jwt


SECRET_KEY="secret123"


ALGORITHM="HS256"



def create_token(data):


    return jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )