introducido = input("Que numero quieres introducir")
nombre = "tabla-n.txt"
file = open("tabla-n.txt".replace("n",introducido),"w")
a=0
for i in range(10):
    file.write(introducido)
    file.write("x")
    i=str(i)
    file.write(i)
    file.write("=")
    a=int(introducido)*int(i)
    file.write(str(a))
    file.write("\n")

os.mkdir[]