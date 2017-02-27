'''
Created on 21/02/2017

@author: ernesto
'''
import logging
import sys
#nivel_log = logging.ERROR
nivel_log = logging.DEBUG
logger_cagada = None

pila_mierda = []
area_max = 0

def recto_largo_saca_caca(pila_mierda):
    return pila_mierda[-1][0]

def recto_largo_core(numero, idx_num):
    global pila_mierda
    global area_max
    if(not pila_mierda):
        logger_cagada.debug("la pila esta vacia, agregando %u(%u)" % (numero, idx_num))
        pila_mierda.append((numero, idx_num))
        if(numero > area_max):
            logger_cagada.debug("el area max era %u aora %u" % (area_max, numero))
            area_max = numero
        return
    
    if(numero > recto_largo_saca_caca(pila_mierda)):
        logger_cagada.debug("el num %u es maior a la punta madre %u" % (numero, pila_mierda[-1][0]))
        pila_mierda.append((numero, idx_num))
        if(numero > area_max):
            area_max = numero
    else:
        limite_izq = -1
        largo_recto_act = 0
        area_act = 0
        while(pila_mierda and numero <= recto_largo_saca_caca(pila_mierda)):
            mierda_sale = pila_mierda.pop()
            logger_cagada.debug(mierda_sale)
            logger_cagada.debug("la mierda q sale %s" % ((mierda_sale),))
        
        if(pila_mierda):
            limite_izq = pila_mierda[-1][1]
            logger_cagada.debug("el idx izq es %u" % limite_izq)
        
        largo_recto_act = idx_num - limite_izq
        
        logger_cagada.debug("el limit izq %u el idx %u el largo del recto %u" % (limite_izq, idx_num, largo_recto_act))
        
        area_act = largo_recto_act * numero
        
        logger_cagada.debug("el num %u y el area %u" % (numero, area_act))
        
        if(area_act > area_max):
            logger_cagada.debug("el area max se actualiza de %u a %u" % (area_max, area_act))
            area_max = area_act
        pila_mierda.append((numero, idx_num))
    
def recto_largo_main():
    lineas = list(sys.stdin)
    global area_max
    global pila_mierda
    
    num_numeros = int(lineas[0])
    numeros = [int(x) for x in lineas[1].strip().split(" ")]
    
    logger_cagada.debug("los nums %s" % numeros)
    
    for idx, num in enumerate(numeros):
        recto_largo_core(num, idx)
        
    ante = 0
    for num, idx in pila_mierda:
        nums_restantes = num_numeros - idx
        area_act = num * nums_restantes
        
        logger_cagada.debug("num %u(%u) ace recto de %u" % (num, idx, area_act))
        
        if(area_act > area_max):
            area_max = area_act
        
        assert ante < num
        
        
    logger_cagada.debug("el area max es %u" % area_max)
    print("%u" % area_max)
        
    
        
if __name__ == '__main__':
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(level=nivel_log, format=FORMAT)
    logger_cagada = logging.getLogger("asa")
    logger_cagada.setLevel(nivel_log)

    recto_largo_main()