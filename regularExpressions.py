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
patron_1 = re.compile("\w{6,20}@(gmail|hotmail)\.com")
#context manager para operar con el archivo de este modo no tenemos que preocuparnos de cerrar el archivo despues de usarlo
#las operaciones con el archivo se hacen dentro de este context manager.
with open('emails.txt', 'r') as doc:
    for line in doc:
        print(line,end="")
    #con este for imprimos cada una de las lineas del archivo que tenemos abierto
    for line in doc:
        if patron_1.search(line): #si el email es valido lanzamos el mensaje y rescatamos el texto coincidente con nuestro patrón
            print("\nESTE CORREO HA SIDO VALDIADO: "+patron_1.search(line).group())
    print("\n******************")


patron_2 = re.compile("\-")
with open('user.txt','r') as doc2:
    for line in doc2:
        print(line, end="")

    for line in doc2:
        patron_2.split(line)
