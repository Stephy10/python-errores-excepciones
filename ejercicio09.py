try:
    entrada=int(input("Ingresa un entero: "))
    
except ValueError:
    print("Haz ingresado un valor no valido, debe ser entero")
else:
    print(entrada)
finally:
    print("Fin de la ejecución")