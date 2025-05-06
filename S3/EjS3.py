usuarios={

}

while True:
    
    ID=input("Ingrese su ID: ")
    Nombre=input("Ingrese su nombre: ")
    Apell=input("Ingrese su apellido: ")
    Correo=input("Ingrese su correo: ")
    usuarios[ID]=[]
    usuarios[ID].append(Nombre)
    usuarios[ID].append(Apell)
    usuarios[ID].append(Correo)

    
    continuar=int(input("¿Desea agregar otro usuario?  1 (si) o 2 (no): "))
    if continuar!=1:
        break


print(usuarios)