#abrir y leer

introducido = input("Que numero quieres introducir")
nombre = "tabla2-n.txt"
file = open("tabla2-n.txt".replace("n",introducido),"w")
a=0
for i in range(11):
    file.write(introducido)
    file.write("x")
    i=str(i)
    file.write(i)
    file.write("=")
    a=int(introducido)*int(i)
    file.write(str(a))
    file.write("\n")
file.close()

file = open(nombre.replace("n",introducido),"r") 
print(file.read())