class Calculadora:
     
            #adicionar dois underscore na frente do atributo priva ele de sofrer alterações __    
          __area_parede = float
          __area_teto = float

          def calcular_area_paredes(self, comodo):
                self.__area_parede = 2 * (comodo.largura + comodo.profundidade) * comodo.altura
                return self.__area_parede
 
                  
          def calcular_area_teto(self, comodo):
                  self.__area_teto = comodo.largura * comodo.profundidade
                  return self.__area_teto

          def calcular_litragem_necessaria(self):
                  if self.__area_parede <=0 or self.__area_teto <=0:
                          print("Não é possivel calcular com esses valores.")
                          exit()
                  return (self.__area_parede + self.__area_teto) / 10  