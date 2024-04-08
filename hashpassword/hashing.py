from passlib.context import CryptContext

pass_hash = CryptContext(schemes=['bcrypt'], deprecated = "auto")

class HashPassword:
    #We hash the password before storing the password
    def hashing(plainpassword: str):
        return pass_hash.hash(plainpassword)
    
    #We verify when login to the account
    def verify_password(plainpassword: str, hashed_password: str):
        return pass_hash.verify(plainpassword, hashed_password)