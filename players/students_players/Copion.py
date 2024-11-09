"""Se basa en buscar un enfoque adaptativo una vez que hay un historial suficiente de jugadas
    Busca a traves del regex patrones similares y en base a las coincidencias decide si va a cooperar de acuerdo a la probabilidadad de que el contrincante coopere """

#libreias
#Importamos la clase Prisonero, random para gener numeros aleatorios y re para trabajar con expresiones regulares
from Prisoner import Prisoner
import random
import re


class Copion(Prisoner):

    #Inicializacion
    def __init__(self):
        
        self.rangoVentanaContricante = 1
        self.rangoVentanaPropio = 2
        self.OffsetHastaEmpezar = 1
        
        self.N = 0 
        
        self.cantidadCooperarContrincante = 0
        self.cantidadTraicionContrincante = 0
        
        self.historialPartidasCompartido = ""
        self.VentanaContricante = ""
        self.VentanaPropio = ""
        
        self.name="Copion"

    @staticmethod
    def name():
        return "Copion"
        
    """
    rangoVentanaContricante: Cuantas decisiones para atras me acuerdo de mi contricante
    rangoVentanaPropio: Cuantas decisiones para atras me acuerdo de mi mismo
    OffsetHastaEmpezar: rondas minimas que deben pasar antes de analizar el historial jugado

    N : Nro. total de rondas 

    cantidadCooperarContrincante: Contador de cuantas veces coopero nuestro contrincante
    cantidadTraicionContrincante: Contador de cuantas veces traiciono nuestro contrincante
    
    historialPartidasCompartido : Historial de las jugadas hasta ahora en formato
                                  MI_JUGADA(N), SU_JUGADA(N), MI_JUGADA(N-1), SU_JUGADA(N-1),...,MI_JUGADA(0), SU_JUGADA(0)
                                  Donde las primeras jugadas del array son las ultimas tomadas                              
    VentanaContricante: Las decisiones recientes del contricante de acuerdo a "rangoVentanaContrincnate"
    VentanaPropio: Las decisiones recientes del contricante de acuerdo a  'rangoVentanaPropio'
    
    name: nombre del bot
    
    
    """

    #Convierte la decision booleana False True a string
    def decisionAString(self,decision):
        if(decision):
            return "T"
        else:
            return "F"
        
    
    #Genera una decision aleatorio en base a probabilidadAFacor
    #Si el numero aleatorio es menor que la probabilidad, devuelve  True sino False     
    def tomarDesicionAleatoria(self, probabilidadAFavor):
        r = random.random() 
        if r < probabilidadAFavor:
            return True
        else:
            return False 
    
    #Se toma la un conjunto de decisiones pasadas y calcula las probabilidades de que el contricante coopere
    #Devuelve la proporcion de las  cooperaciones 
    def medirProbabilidad(self, decisionesPasadas):
        contadorTraicionar = 0
        contadorCooperar = 0
        for estadoPasado in decisionesPasadas:
            JugadaSiguienteOponente = estadoPasado[1]
            if(JugadaSiguienteOponente == "T"):
                contadorCooperar += 1
            else:
                contadorTraicionar += 1
        
        return (contadorCooperar / (contadorTraicionar + contadorCooperar))
        
    #Decide la estrategia a tomar
    def pick_strategy(self):
        
        # Si el historial aun no esta grande como para haber recolectado informacion, coopero
        if(self.N < max(self.rangoVentanaContricante, self.rangoVentanaPropio) + self.OffsetHastaEmpezar):
            return True
        else:
            # Si ya hay un historial suficiente, busco una instancia donde hubo un estado de juego similar
            # Es decir, donde se tomaron las mismas decisiones hasta ahora.
            # Suponemos que el contricante hara algo similar a lo que hizo la ultima vez.
            # Cuanto mas grande sean las ventanas, mayor sera el contexto que se toma en cuenta en la busqueda.
            
            # Inicializamos la query por regex y pasamos por nuestras ultimas jugadas completando la query
            queryUltimaJugadaParecida = r''
            for jugadaPasadaIndex in range(max(self.rangoVentanaContricante, self.rangoVentanaPropio)):
                
                #Decisiones propias
                #Añadimos la jugada o sino "." que funciona como cualquier jugada
                if jugadaPasadaIndex < self.rangoVentanaPropio:
                    queryUltimaJugadaParecida += self.VentanaPropio[jugadaPasadaIndex]
                else:
                    queryUltimaJugadaParecida += '.'
                
                #Decisiones del contrincante 
                #Añadimos la jugada o sino "."
                if jugadaPasadaIndex < self.rangoVentanaContricante:
                    queryUltimaJugadaParecida += self.VentanaContricante[jugadaPasadaIndex]
                else:
                    queryUltimaJugadaParecida += '.'
            
            # Agregamos dos comodines al principio para solo tomar en cuenta estados donde conocemos el resultado siguiente
            queryUltimaJugadaParecida = '.' + queryUltimaJugadaParecida
            queryUltimaJugadaParecida = '.' + queryUltimaJugadaParecida
            
            # Encontramos en el historial todas las instancias de este estado y lo que paso luego
            UltimasJugadasParecidas = re.findall(queryUltimaJugadaParecida, self.historialPartidasCompartido)
            

            # Tomamos una decision en base a la busqueda
            # Si no hay coincidencias, hacemos una eleccion aleatoria segun el pasado de nuestro contrincante.
            # Vemos cuantas veces coopero y hacemos una proporcion del total
            if(len(UltimasJugadasParecidas) == 0):
                porcentajeGlobal = self.cantidadCooperarContrincante / self.N
                return self.tomarDesicionAleatoria(porcentajeGlobal)
            else:
                # En caso contrario, copiamos la decision del contrincante, evadiendo perder puntos y manteniendo la cooperacion
                # Para esto, buscamos la decision mas probable que tome y decidimos segun esta misma probabilidad.
                ProbabilidadDeCopeerar = self.medirProbabilidad(UltimasJugadasParecidas)
                return self.tomarDesicionAleatoria(ProbabilidadDeCopeerar)
               
            

    def process_results(self, my_strategy, other_strategy):
        
        # Aumentamos el numero de partida 
        self.N += 1
        
        #Actualizamos historial de jugadas con jugadas mas reciuentes al principio
        self.historialPartidasCompartido = self.decisionAString(my_strategy) + self.decisionAString(other_strategy) + self.historialPartidasCompartido
        
        #Regustro del contrincante
        if(self.N <= self.rangoVentanaContricante):
            self.VentanaContricante = self.decisionAString(other_strategy) + self.VentanaContricante 
        else:
            self.VentanaContricante = self.decisionAString(other_strategy) + self.VentanaContricante 
            self.VentanaContricante = self.VentanaContricante[:-1] #Recortamos la cadena
            
        #Registro propio
        if(self.N <= self.rangoVentanaPropio):
            self.VentanaPropio = self.decisionAString(my_strategy) + self.VentanaPropio 
        else:
            self.VentanaPropio = self.decisionAString(my_strategy) + self.VentanaPropio 
            self.VentanaPropio = self.VentanaPropio[:-1]#Recortamos la cadena
            
        #Actualizamos el contador de las deciiones del contrincante
        if(other_strategy):
            self.cantidadCooperarContrincante += 1
        else:
            self.cantidadTraicionContrincante += 1