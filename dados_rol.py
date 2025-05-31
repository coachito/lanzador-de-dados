import random         
import time
lista_caras = [
               "4. Caras", "5. Caras", "6. Caras", "7. Caras", "8. Caras",
                 "9. Caras", "10. Caras","11. Caras", "12. Caras", "13. Caras", "14. Caras", 
                 "15. Caras", "16. Caras", "17. Caras", "18. Caras", "19. Caras", "20. Caras"]
adjetivos = ["Discordia", "Desdicha", "Valentia", "Metastasis", "Muerte", "Leyenda"]
curses = ["Envenenado", "Herido", "Incapacitado por 1 Turno", "Aturdido"]
buffs = ["Equipo Gana un 20'%' de Ataque extra", "equipo se cura un 50'%' de la vida Max", 
         "personaje consigue un turno extra", "personaje se cura un 20'%' de su vida max"]
def display(opciones):
    print("""\nBienvenido al lanzador de Dados creado por Camilo Ortegon
    \nEste lanzador te ayudara a lanzar dados segun sus caras para tu grandioso juego de ROL!\n\n-¡Les deseo una Gran Aventura!\n""")
    for p, o in enumerate(opciones, start=1):
        print(f"{p}. {o}")
def lanzar():
    while True:
        try:
            caras = int(input("¿De cuántas caras será el dado? (entre 4 y 20): "))
            cant = int(input("¿Cuántos dados lanzarás?: "))
            if caras < 4 or caras > 20:
                print("Número de caras no válido. Intenta nuevamente.")
            else:
                break
        except ValueError:
            print("Solo ingresa números.")

    while True:
        total = 0

        for i in range(1, cant + 1):
            s = random.choice(adjetivos)
            print(f"\nLanzando el dado de la {s}...")
            time.sleep(2)

            resultado = random.randint(1, caras)
            total += resultado

            print(f"\n🎲 Dado número {i} tiene el resultado: {resultado}")
            time.sleep(1)

            if resultado <= 4:
                print("❌ ¡Fallo épico!")
            elif resultado <= 10:
                print("⚔️ Golpe normal")
            else:
                print("💥 ¡Golpe Crítico!")
            time.sleep(1)

        print(f"\n🔢 El resultado total de tus dados es: {total}")
        time.sleep(1)

        if total < 10:
            b = random.choice(curses)
            print(f"\n💀 Tu personaje sufre: {b}")
        else:
            c = random.choice(buffs)
            print(f"\n💫 Tu {c}")
        time.sleep(2)

        # PREGUNTA PARA REPETIR LA MISMA TIRADA
        repetir = input("\n¿Quieres volver a lanzar los mismos dados? (s/n): ").lower()
        if repetir != "s":
            break

    return caras, cant


def vercaras():
    for i in lista_caras:
        print(f"\n {i}")

        
        time.sleep(0.5)


while True:
    display(["Lanzar Dados", "Ver dados disponibles", "Salir\n"])
    opcion = int(input("Elige una opción de 1-3: \n"))

    if opcion == 1:
            lanzar()
    elif opcion == 2:
        vercaras()
    elif opcion ==3:
        break
    else:
        print("No esta esa opción, porfavor vuelve a intentar")    
    