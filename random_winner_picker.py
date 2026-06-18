import random

#variable 
participantes = ["Celeste", "Andrea", "Rojas", "Chema", "Pame", "Lalo", "Peluche"]

 # preguntar si quiere agregar nombres
respuesta = input("¿Quieres agregar un nombre? (si/no): ").strip().lower()

#append

while respuesta == "si":
    nuevo = input("Ingresa el nombre: ")
    participantes.append(nuevo)
    
    print("Lista actual:", participantes)
    
    respuesta = input("¿Quieres agregar otro nombre? (si/no): ").strip().lower()
    
    print("Lista actual:", participantes) 


#remove
#choice
#remove
#append

 while len(participantes) > 0:
    ganador = choice(participantes)
    participantes.remove(ganador)
    
    print("Ganador:", ganador)
    print("Restantes:", participantes) 



while participantes:
    input("Presiona ENTER para sacar un ganador...")  # 👈 pausa ANTES
    
    ganador = random.choice(participantes)
    participantes.remove(ganador)
    
    print("Ganador:", ganador)
    print("Restantes:", participantes)
   
    