#tabla nxm

n= input("Introduce un numero del 1 al 10")
m= input("introduce otro numero del 1 al 10")
archivo= "tabla-nxm.txt"
archivo.replace("m",m)
file = open(archivo.replace("n",n),"w")

a=0
for i in range(11):
    file.write(m)
    file.write("x")
    i=str(i)
    file.write(i)
    file.write("=")
    a=int(m)*int(i)
    file.write(str(a))
    file.write("\n")

file.close()
file = open(archivo.replace("n",n),"r") 

lineas = file.readlines()
print(lineas[int(n)])
