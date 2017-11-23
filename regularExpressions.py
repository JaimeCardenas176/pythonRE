# -*- coding: utf-8 -*-
"""
. un caracter excepto nueva linea \n
\r retorno de acarreo
\t tabulador horizontal
\w cualquier caracter alfanumerico
\W caracter alfanumerico mayusculas
\s espacio en blanco
\S cualquier caracter que no es espacio en blanco
\d 0-9
\D !0-9
^ inicio de cadea
$ fin de cadena
\ escape de caracteres especiales

[] rango
^[] cualquier caracter que no este entre corchetes
\b separacion entre numero y o letra
+ una o mas veces
* 0 o mas veces
? 0 o 1 vez
{n} numero de veces
"""

import re
patron_1 = re.compile("\D{6,20}@(gmail|salesianos)\.(com|edu)", re.I)#construimos un patron con compile() ademas le estamos pasando re.I (IGNORECASE) en este caso para validar emails
#context manager para operar con el archivo de este modo no tenemos que preocuparnos de cerrar el archivo despues de usarlo
#las operaciones con el archivo se hacen dentro de este context manager.
with open('emails.txt', 'r') as doc:
    # con este for imprimos cada una de las lineas del archivo que tenemos abierto
    for line in doc:
        print(line, end="")
print("\n******************")#fin de la impresion

with open('emails.txt', 'r') as docx:
    for line in docx:
        if patron_1.search(line): #si el email es valido lanzamos el mensaje y rescatamos el texto coincidente con nuestro patrón
            print("\nESTE CORREO HA SIDO VALIDADO: "+patron_1.search(line).group())
    print("\n******************")


patron_2 = re.compile("(\-|\n)")
#context manager!
with open('user.txt','r') as doc2:
    for line in doc2:
        print(line, end="")
    print("\n******************")
with open('user.txt', 'r') as doc2x:
    for line in doc2x:
        print (patron_2.split(line))#nos devuelve la lista del texto troceado a partir de la re
    print("\n******************")

nombre = re.compile("JULES")
with open('guion.txt','r') as doc3:
    for line in doc3:
        print(line, end="")
    print("\n******************")
with open('guion.txt', 'r') as doc3x:
    for line in doc3x:
        print(nombre.sub("MANOLO", line, re.I))#nos devuelve el texto ya cambiado ignorando ademas mayusculas.
    print("\n******************")


patron_3 = re.compile("^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$")#este es el formato de validación de las url
with open('urls.txt', 'r') as doc4:
    for line in doc4:
        print(line, end="")
    print("\n******************")

with open('urls.txt', 'r') as doc4x:
    print("listado de urls validadas")
    for line in doc4x:
        if patron_3.match(line):
            print(patron_3.match(line).group())
    print("\n******************")


patron_4 = re.compile("^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[012])/((19|20)\d\d)$")#este es un formato que podria valr para validar fechas
with open('user.txt', 'r') as doc5:
    for line in doc5:
        print(line, end="")
    print("\n******************")

with open('user.txt', 'r') as doc5x:
    for line in doc5x:
        lista = []
        lista = patron_2.split(line)
        if patron_4.search(lista[6]):
            print(patron_4.search(lista[6]).group())
    print("\n******************")
