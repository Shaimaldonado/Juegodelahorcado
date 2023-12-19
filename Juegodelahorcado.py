import random  #escoge la palabra en el juego
def palabra_a_adivinar ():
    palabras = [
    'amarillo'
]   #el juego va a elegir una de las palabras ingresadas
    palabra_al_azar=random.choice(palabras)
    return palabra_al_azar

def formato_del_juego(PalabraBuscada,LetrasBuscadas):
    juego=""
    for letra in PalabraBuscada:
        if letra in LetrasBuscadas:
            juego +=letra
        else:
            juego+="_"
    print(juego)
    
def juego_del_ahorcado():
    PalabraBuscada= palabra_a_adivinar()
    LetrasBuscadas= []
    Intentos=10
    
    while Intentos>0:
        formato_del_juego(PalabraBuscada,LetrasBuscadas)
        letra=input("Ingresa una letra: ").lower()
        
        if letra in LetrasBuscadas:
            print("Ya intentaste con esta letra")  
            continue
        if letra in PalabraBuscada:
            LetrasBuscadas.append(letra)
            if set (LetrasBuscadas)==set(PalabraBuscada):
                print("Bien, adivinaste correctamente")
                break
            
        else:
            Intentos-=1
            print(f"Perdiste una vida, intenta nuevamente. Te quedan: {Intentos} restantes")
    if Intentos==0:
        print("Perdiste el juego")
        print(f"La pabrabra era : {PalabraBuscada}")
        
juego_del_ahorcado() #para que corra el programa  