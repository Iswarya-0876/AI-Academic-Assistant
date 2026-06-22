from argon2 import PasswordHasher


ph = PasswordHasher()



def hash_password(password: str):

    return ph.hash(password)





def verify_password(
    plain_password: str,
    hashed_password: str
):

    try:

        ph.verify(
            hashed_password,
            plain_password
        )

        return True


    except:

        return False