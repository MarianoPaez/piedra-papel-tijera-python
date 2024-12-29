nombre1 = input("¿Como se llama el judaror 1?: ")
nombre2 = input("¿Como se llama el judaror 2?: ")


jugador1 = input("hola jugador 1! ¿que eliges? ¿piedra, papel o tijera?")
jugador2 = input("hola jugador 2! ¿que eliges? ¿piedra, papel o tijera?")

condicion1 = jugador1 == "piedra" and jugador2 == "tijera"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijera" and jugador2 == "papel"

if jugador1 == jugador2:
    print("ha sido un empate!")
elif condicion1 or condicion2 or condicion3:
    print("ha ganado:" , nombre1)
else:
    print("ha ganado:", nombre2)