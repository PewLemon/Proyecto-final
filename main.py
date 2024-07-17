print("Bienvenido a la sección de personalización de su personaje")
personalizacion = []
#Sistema de personalización de los aspectos faciales del personje
print("\nElige las características faciales de tu personaje:\n1. Nariz chata\n2. Nariz respingosa\n3. Nariz pronunciada")
nariz = input("Ingrese el número de su elección: ")
if nariz == "1":
    personalizacion.append("Nariz chata")
elif nariz == "2":
    personalizacion.append("Nariz respingosa")
elif nariz == "3":
    personalizacion.append("Nariz pronunciada")
else:
    print("La opción ingresada no es válida, se ajustará a sin selección")
    personalizacion.append("Sin selección")
#Sistema de personalización del color de ojos del personaje
print("\nElige el color de los ojos de tu personaje:\n1. Azul\n2. Verde\n3. Marrón\n4. Negro")
ojos = input("Ingrese el número de su elección: ")
if ojos == "1":
    personalizacion.append("Ojos azules")
elif ojos == "2":
    personalizacion.append("Ojos verdes")
elif ojos == "3":
    personalizacion.append("Ojos marrones")
elif ojos == "4":
    personalizacion.append("Ojos negros")
else:
    print("La opción ingresada no es válida, se ajustará a sin selección")
    personalizacion.append("Sin selección")
#Sistema de elección del tipo de cuerpo del personaje
print("\nElige el tipo de cuerpo de tu personaje:\n1. Flaco\n2. Promedio\n3. Musculoso\n4. Mamado")
cuerpo = input("Ingrese el número de su elección: ")
if cuerpo == "1":
    personalizacion.append("Cuerpo flaco")
elif cuerpo == "2":
    personalizacion.append("Cuerpo promedio")
elif cuerpo == "3":
    personalizacion.append("Cuerpo musculoso")
elif cuerpo == "4":
    personalizacion.append("Cuerpo mamado")
else:
    print("La opción ingresada no es válida, se ajustará a sin selección")
    personalizacion.append("Sin selección")
#Sistema de elección del tipo de armadura para el personaje base
print("\nElige la armadura de tu personaje:\n1. Escamas de dragón\n2. Armadura de cuero\n3. Armadura de acero\n4. Armadura romana")
armadura = input("Ingrese el número de su elección: ")
if armadura == "1":
    personalizacion.append("Armadura de escamas de dragón")
elif armadura == "2":
    personalizacion.append("Armadura de cuero")
elif armadura == "3":
    personalizacion.append("Armadura de acero")
elif armadura == "4":
    personalizacion.append("Armadura romana")
else:
    print("La opción ingresada no es válida, se ajustará a sin selección")
    personalizacion.append("Sin selección")
#Sistema de elección del arma del personaje
print("\nElige el tipo de arma de tu personaje:\n1. Espada\n2. Arco\n3. Hacha\n4. Ballesta\n5. Puño limpio\n6. Flecha normal\n7. Flecha encantada\n8. Flecha venenosa")
arma = input("Ingrese el número de su elección: ")
if arma == "1":
    personalizacion.append("Espada")
elif arma == "2":
    personalizacion.append("Arco")
elif arma == "3":
    personalizacion.append("Hacha")
elif arma == "4":
    personalizacion.append("Ballesta")
elif arma == "5":
    personalizacion.append("Puño limpio")
elif arma == "6":
    personalizacion.append("Flecha normal")
elif arma == "7":
    personalizacion.append("Flecha encantada")
elif arma == "8":
    personalizacion.append("Flecha venenosa")
else:
    print("La opción ingresada no es válida, se ajustará a sin selección")
    personalizacion.append("Sin selección")
#Sistema de elección de raza del personaje
print("\nElige la raza de tu personaje:\n1. Dios\n2. Elfo\n3. Enano\n4. Mestizo\n5. Afrodescendiente\n6. Descendencia asiática\n7. Descendencia occidental")
raza = input("Ingrese el número de su elección: ")
if raza == "1":
    personalizacion.append("Dios")
elif raza == "2":
    personalizacion.append("Elfo")
elif raza == "3":
    personalizacion.append("Enano")
elif raza == "4":
    personalizacion.append("Mestizo")
elif raza == "5":
    personalizacion.append("Afrodescendiente")
elif raza == "6":
    personalizacion.append("Descendencia asiática")
elif raza == "7":
    personalizacion.append("Descendencia occidental")
else:
    print("La opción ingresada no es válida, se ajustará a sin selección")
    personalizacion.append("Sin selección")
#Sistema de elección del color de cabello del personaje
print("\nElige el color del cabello de tu personaje:\n1. Negro\n2. Marrón\n3. Rubio\n4. Pelirrojo\n5. Blanco\n6. Tornasol")
cabello = input("Ingrese el número de su elección: ")
if cabello == "1":
    personalizacion.append("Cabello negro")
elif cabello == "2":
    personalizacion.append("Cabello marrón")
elif cabello == "3":
    personalizacion.append("Cabello rubio")
elif cabello == "4":
    personalizacion.append("Cabello pelirrojo")
elif cabello == "5":
    personalizacion.append("Cabello blanco")
elif cabello == "6":
    personalizacion.append("Cabello tornasol")
else:
    print("La opción ingresada no es válida, se ajustará a sin selección")
    personalizacion.append("Sin selección")
#Sistema de elección para el tipo de ropa del personaje
print("\nElige el tipo de vestimenta de tu personaje:\n1. Pantalón largo\n2. Pantaloneta\n3. Falda\n4. Camiseta\n5. Chaqueta\n6. Manga corta\n7. Manga larga\n8. Sin manga")
vestimenta = input("Ingrese el número de su elección: ")
if vestimenta == "1":
    personalizacion.append("Pantalón largo")
elif vestimenta == "2":
    personalizacion.append("Pantaloneta")
elif vestimenta == "3":
    personalizacion.append("Falda")
elif vestimenta == "4":
    personalizacion.append("Camiseta")
elif vestimenta == "5":
    personalizacion.append("Chaqueta")
elif vestimenta == "6":
    personalizacion.append("Manga corta")
elif vestimenta == "7":
    personalizacion.append("Manga larga")
elif vestimenta == "8":
    personalizacion.append("Sin manga")
else:
    print("La opción ingresada no es válida, se ajustará a sin selección")
    personalizacion.append("Sin selección")
#Sistema de elección del elemento del personaje
print("\nElige el elemento de tu personaje:\n1. Fuego\n2. Agua\n3. Tierra\n4. Aire\n5. Madera")
elemento = input("Ingrese el número de su elección: ")
if elemento == "1":
    personalizacion.append("Elemento fuego")
elif elemento == "2":
    personalizacion.append("Elemento agua")
elif elemento == "3":
    personalizacion.append("Elemento tierra")
elif elemento == "4":
    personalizacion.append("Elemento aire")
elif elemento == "5":
    personalizacion.append("Elemento madera")
else:
    print("La opción ingresada no es válida, se ajustará a sin selección")
    personalizacion.append("Sin selección")
#Sistema de elección del tipo de clase del personaje
print("\nElige la clase de tu personaje:\n1. Guerrero\n2. Mago\n3. Arquero\n4. Héroe")
clase = input("Ingrese el número de su elección: ")
if clase == "1":
    personalizacion.append("Guerrero")
elif clase == "2":
    personalizacion.append("Mago")
elif clase == "3":
    personalizacion.append("Arquero")
elif clase == "4":
    personalizacion.append("Héroe")
else:
    print("La opción ingresada no es válida, se ajustará a sin selección")
    personalizacion.append("Sin selección")
#Imprimir todas las elecciones anteriores
print("\nHa terminado la personalización, listo para jugar?")
print("Resumen de tu personalización:")
print(", ".join(personalizacion))