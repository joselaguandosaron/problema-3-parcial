import random
import time

'''
En una urbanización se van a construir casas de dos tipos; A y B. La empresa constructora
dispone para ello de un máximo de 18 millones de euros, siendo el coste de cada tipo de casa de
300000 euros y 200000 euros, respectivamente. El ayuntamiento exige que el número total de
casas no sea superior a 80. Sabiendo que el beneficio obtenido por la venta de una casa de tipo A
es de 40000 euros y de 30000 euros por una del tipo B. ¿cuántas casas deben construirse de cada
tipo para obtener el máximo beneficio?
'''

def problema_3():
   inicio=time.time()
   contadore=0
   while True:
    contadore+=1
    casa_a=300000
    casa_b=200000

    empresa_dinero=18000000
    limite_de_casas=80

    beneficio_de_casa_a=40000
    beneficio_de_casa_b=30000

    beneficio_ganancia=0
    dinero_gastado=0
    contador_de_casa=0

    casa_contruida_a=0
    casa_contruida_b=0

    while contador_de_casa<limite_de_casas and dinero_gastado<empresa_dinero :
        contruir_casa=random.choice((casa_a,casa_b))
        if contruir_casa==200000:
            dinero_gastado+=200000
            beneficio_ganancia+=beneficio_de_casa_b
            casa_contruida_b+=1
        if contruir_casa==300000:
            dinero_gastado+=300000
            beneficio_ganancia+=beneficio_de_casa_a
            casa_contruida_a+=1

        contador_de_casa+=1
    if contador_de_casa==80 and dinero_gastado==empresa_dinero :
     print("maximo_beneficio:",beneficio_ganancia)
     print("casa contruida a:",casa_contruida_a)
     print("casa contruida b:", casa_contruida_b)
     print("total de casas contruidas:",contador_de_casa)
     print("dinero gastado total:",dinero_gastado)
     print("Numero de ejecuciones:",contadore)
     fin=time.time()
     print("tiempo de ejecucion:",fin-inicio)
     return True

problema_3()
