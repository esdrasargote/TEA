#Tendencias e Innovación en Tecnología Agrícola
try:
    puntos= float(input("Ingrese Puntuación: "))

    if puntos< 0.0 or puntos > 1.0:
        print("Puntuacion incorrecta")
    else:
        if puntos >= 0.9:
            print("Sobresaliente")
        elif puntos >= 0.8 and puntos < 0.9:
            print('Notable')
        elif puntos >= 0.7 and puntos < 0.8:
            print('Bien')
        elif puntos >= 0.6 and puntos < 0.7:
            print('Suficiente')
        else:
                print('Insuficiente')
except:
    print("Puntuacion incorrecta")
