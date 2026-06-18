#diccionario de valores
valores={ 
    "1": 1, "2": 2, "3": 3, "4": 4, "5": 5
}

def dameLosNumeros():
    numeros = (input("Ingresa tu serie numerica(5 números solamente): "))
    return numeros

def costo(numeros):
    total = 0
    for digito in numeros:
        total += valores.get(digito, 0)
    return total

def cambio(total):      
    dineroRecibido=int(input("recibo "))
    cambio = dineroRecibido - total
    return cambio
    
def inteDeCambio(cambio_):
    cambio_= cambio(cambio_)

    if cambio_ > 0:
        print(f"tu cambio es {cambio_}")
    elif cambio_ == 0:
        print("pago exacto")
    else:
        print(f"te falta")

def ejecutarTodo():
    queQuieres= (input("hola, le checo el precio (si/no): "))

    if queQuieres == "si":
        print("perfecto")

        numeros = dameLosNumeros()
        total= costo(numeros)

        print(f"el costo es {total}")
        print("deseas pagar o seguir viendo")
        opcion = input("(pagar/seguir): ")

        if opcion == "pagar":
            
            inteDeCambio(total)
            print("gracias por la compra")
        else:
            print("siga viendo")
    
    else:
        print ("siga viendo")

ejecutarTodo()