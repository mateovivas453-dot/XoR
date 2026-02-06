def cifrado_xor(texto, clave):

    if isinstance(texto, str):
        texto = texto.encode()

    if isinstance(clave, str):
        clave = clave.encode()

    if len(clave) < len(texto):
        clave = clave * (len(texto) // len(clave) + 1)
        clave = clave[:len(texto)]

  
    return bytes([t ^ c for t, c in zip(texto, clave)])


texto_original = "Hola Mundo!"
llave = "secreto"

mensaje_cifrado = cifrado_xor(texto_original, llave)
print("Cifrado:", mensaje_cifrado)

mensaje_descifrado = cifrado_xor(mensaje_cifrado, llave)
print("Descifrado:", mensaje_descifrado.decode())

