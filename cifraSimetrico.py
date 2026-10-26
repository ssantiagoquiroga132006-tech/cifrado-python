from cryptography.fernet import Fernet

def generar_clave_simetrica() -> bytes:
    return Fernet.generate_key()

def cifrar_texto_simetrico(mensaje: str, clave: bytes) -> bytes:
    f = Fernet(clave)
    return f.encrypt(mensaje.encode('utf-8'))

def descifrar_texto_simetrico(token_cifrado: bytes, clave: bytes) -> str:
    f = Fernet(clave)
    return f.decrypt(token_cifrado).decode('utf-8')