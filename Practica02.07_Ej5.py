# PIB

pais= input("Introduzca las iniciales del pais a mostrar").upper()


archivo_PIB= open("C:/datos/Documents/GIT_svelasqpum/ficherointernauta/estat_sdg_08_10.tsv","r")

for linea in archivo_PIB:
    if pais in linea:
        print(linea)
 
    