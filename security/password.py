from argon2 import PasswordHasher


ph=PasswordHasher()


def hash_password(password):

    return ph.hash(password)



def verify_password(
    password,
    hashed
):

    try:

        ph.verify(
            hashed,
            password
        )

        return True

    except:

        return False