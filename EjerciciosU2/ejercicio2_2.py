def password(code: str):
    varcon = code.lower()
    con = input("Introduce la contraseña: ")
    con = con.lower()
    if (varcon == con):
        return "La contraseña introducida coincide con la contraseña guardada."
    else:
        return "La contraseña introducida no coincide con la contraseña guardada."

contra = input("Introduce una contraseña para guardar: ")
print(password(contra))