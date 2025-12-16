# Codifique un juguete
nombre = input("¿Cuál es tu nombre? ")
puesto = input("¿Cuál es el nombre de tu puesto? ")
adj_uno = input("Escribe un adjetivo acerca del rol: ")
adj_dos = input("Escribe un adjetivo que describa al profesor: ")
comida_uno = input("¿Qué comes en las mañanas? ")
comida_dos = input("¿Qué comes en la hora de la comida? ")
sentimiento = input("¿Qué sentimiento presentaste al comenzar este curso? ")

# Creando historias locas
print()
print("Esta es tu historia loca: ")
print()
print(f"""{nombre} ha comenzado hoy su primer curso de generation. Se están formando como {puesto}. Su compañero les 
pareció muy {adj_uno}, pero su profesor era, cuando menos, {adj_dos}. Para comer comen {comida_uno} y {comida_dos} mientras
repasan sus notas. Sienten {sentimiento} pero están decididos a completar el curso""")
