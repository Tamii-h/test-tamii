nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Introduzca su edad: ")
telefono = input("Ingrese su numero de telefono: ")
email = input("Introduzca su direccion de email: ")
print("***********************************************************")
print("Su nombre es", nombre + " " + apellido + ". Tiene", edad + " años.")
print("Numero de telefono:", telefono)
print("Email:", email)
print("***********************************************************")
# ----------------------------------- -------------------------------------------
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

promedio = (num1+num2+num3)/3

print("El promedio de los numeros ingresados es:", promedio)

# ---------------------------------------- --------------------------------------
#from io import RawIOBase

#Programa que le pida ingresar 4 colores. Mostrarlos por consola.
col1 = input("Ingresar color: ")
col2 = input("Ingresar el segundo color: ")
col3 = input("Ingrese el tercer color: ")
col4 = input("Ingrese el cuarto color: ")

colores = [col1, col2, col3, col4]
print("Los colores ingresados son:", colores)

#Agregarle un color desde el programa, mostrarle al usuario el nuevo color agregado. 
nuvoCol = input("Añadir un nuevo color: ")

colores.append(nuvoCol)
print("El color ingresado fue el:", nuvoCol+"\nListado de colores:", colores)

#Imprimir la cantidad de colores.
print("Cantidad de colores ingresados:", len(colores))

#Pedirle al usuario que ingrese un nuevo color e insertarlo en la posición 1. Imprimir el listado de colores.
col5 = input("Ingrese otro color: ")

colores.insert(1, col5)
print("Listado de colores:", colores)

#Mostrale por consola al usuario el color que se encuentra en la posicion 3.
print("En la posicion tres se encuentra el color:", colores[3])

#Eliminar el ultimo color de la lista.
print("Lista actual:", colores)
colores.pop()
print("Lista eliminando el ultimo color:", colores)

#Pedirle al usuario que ingrese un color para ver si existe en la lista, imprimir por consola Verdadero o Falso. 
colBuscar = input("¿Cuales el color que desea buscar en la lista?:")

if colBuscar in colores:
    print("El color", colBuscar,"si se encuantra en la lista \n\t VERDADERO")

if colBuscar not in colores:
    print("El color", colBuscar,"no se encuantra en la lista \n\t FALSO")

#Limpiar la lista e imprimirla por consola.
colores.clear()
print("Lista colores:",colores)