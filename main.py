from calculadora import Calculadora
from comodo import Comodo

calc = Calculadora()

#removi os inputs que foram adicionados incialmente para fazer a chamada direto do objeto
#DETALHE COLOCAR VIRGULA QUANDO TIVER MAIS DE UM INPUT É BOBO MAS EU ESQUECI KKKK
comodo = Comodo(
    input("Qual a largura do cômodo? "),
    input("Qual a profundidade do cômodo? ")
)

#removi a variavel comodo pois ela já está inclusa no objeto comodo


#calc.area_parede: float = 2 * (largura + profundidade)* altura


#saida de dados
print("A área das paredes é:  ", calc.calcular_area_paredes(comodo))
print("A área do teto é: ", calc.calcular_area_teto(comodo))
print("A litragem de tinta necessária é:" , calc.calcular_litragem_necessaria())

