from jose import jwt


SECRET="AI_SECRET"


def create_token(data):

    return jwt.encode(
        data,
        SECRET,
        algorithm="HS256"
    )