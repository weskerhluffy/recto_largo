'''
Created on 21/02/2017

@author: ernesto
'''
import logging
import sys
nivel_log = logging.ERROR
#nivel_log = logging.DEBUG
logger_cagada = None

pila_mierda = []
area_max = 0

def recto_largo_saca_caca(pila_mierda):
    return pila_mierda[-1][0]

def recto_largo_saca_caca_idx(pila_mierda):
    return pila_mierda[-1][1]

def recto_largo_core(numero, idx_num):
    global pila_mierda
    global area_max
    
    limite_izq = -1
    largo_recto_act = 0
    area_act = 0
    
    limite_der_ass = idx_num - 1
    while(pila_mierda and numero <= recto_largo_saca_caca(pila_mierda)):
        limite_izq_ass = -1
        mierda_sale = pila_mierda.pop()
        logger_cagada.debug("la mierda q sale %s, numact %u" % ((mierda_sale), numero))
        if(pila_mierda):
            limite_izq_ass = recto_largo_saca_caca_idx(pila_mierda) 
        num_sale = mierda_sale[0]
        logger_cagada.debug("el num q sale %u, limites %u-%u" % (num_sale, limite_izq_ass, limite_der_ass))
        
        tam_recto_ass = limite_der_ass - limite_izq_ass
        
        area_ass = tam_recto_ass * num_sale
        
        logger_cagada.debug("el tamm recto es %u, el area %u" % (tam_recto_ass, area_ass))
        
        if(area_ass > area_max):
            area_max = area_ass
        
    if(pila_mierda):
        limite_izq = recto_largo_saca_caca_idx(pila_mierda)
        logger_cagada.debug("el idx izq es %u, num %u" % (limite_izq, recto_largo_saca_caca(pila_mierda)))
        
    largo_recto_act = idx_num - limite_izq
        
    logger_cagada.debug("el limit izq %u el idx %u el largo del recto %u" % (limite_izq, idx_num, largo_recto_act))
        
    area_act = largo_recto_act * numero
        
    logger_cagada.debug("el num %u y el area %u" % (numero, area_act))
        
    if(area_act > area_max):
        logger_cagada.debug("el area max se actualiza de %u a %u" % (area_max, area_act))
        area_max = area_act
        
    pila_mierda.append((numero, idx_num))
    
def recto_largo_calcula_a_la_mala(numeros):
    num_numeros = len(numeros)
    area_max_a = 0
    
    for i in range(0, num_numeros):
#        logger_cagada.debug("donde estan %u" % i)
        for j in range(i, num_numeros):
#            logger_cagada.debug("calculando de %u a %u" % (i, j))
            cacas = numeros[i:j + 1]
            alt_max = min(cacas)
            area_actu = alt_max * len(cacas)
            if(area_actu == 342):
                logger_cagada.debug("a la mierda %u,%u con alt max %u" % (i, j, alt_max))
            if(area_actu > area_max_a):
                area_max_a = area_actu
    
    logger_cagada.debug("area max a la brava %u" % area_max_a)
    return area_max_a
            
            

    
def recto_largo_main():
    lineas = list(sys.stdin)
    global area_max
    global pila_mierda
    
    num_numeros = int(lineas[0])
    numeros = [int(x) for x in lineas[1].strip().split(" ")]
    
    assert num_numeros == len(numeros)
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
    
    if(nivel_log==logging.DEBUG):
        shit = recto_largo_calcula_a_la_mala(numeros)
    
        assert shit == area_max, "la mierda debug %u, el area max %u" % (shit, area_max)
    
    print("%u" % area_max)
        
    
        
if __name__ == '__main__':
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(level=nivel_log, format=FORMAT)
    logger_cagada = logging.getLogger("asa")
    logger_cagada.setLevel(nivel_log)

    recto_largo_main()
