import secrets, string

diccionario = {
    'letras': string.ascii_letters,
    'numeros': string.digits,
    'caracteres': string.punctuation
}
print("/////////////////////////////////////")
print("VAS A GENERAR UNA NUEVA CONTRASEÑA")
print("/////////////////////////////////////")

largo = int(input("¿Cuántos caracteres querés? "))

# aceptamos "s", "si", "S", " SI ", etc.
usar_letras = input("¿Incluir letras? (s/n): ").strip().lower().startswith("s")
usar_numeros = input("¿Incluir números? (s/n): ").strip().lower().startswith("s")
usar_caracteres = input("¿Incluir caracteres especiales? (s/n): ").strip().lower().startswith("s")

tipos = []
if usar_letras:
    tipos.append(diccionario['letras'])
if usar_numeros:
    tipos.append(diccionario['numeros'])
if usar_caracteres:
    tipos.append(diccionario['caracteres'])

if len(tipos) == 0:
    print("No elegiste ningún tipo de carácter.")
else:
    password = ""
    for i in range(largo):
        tipo = secrets.choice(tipos)
        password += secrets.choice(tipo)

    print("\nTU NUEVA CONTRASEÑA ES:")
    print(password)


