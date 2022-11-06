import hashlib, base64

def codificar_senha(senha):
    #Retorna a variável de entrada codificada
    senha_encoded = senha.encode('utf-8')
    digest = hashlib.sha512(senha_encoded).digest()
    digest_b64_encoded = base64.b64encode(digest)
    digest_b64_encoded_utf8_decoded = digest_b64_encoded.decode('utf-8')
    return digest_b64_encoded_utf8_decoded