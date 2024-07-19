# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

var1 = int(input("\n qual operacao deseja fazer? \n 1 = mais \n 2 = menos \n 3 = vezes \n 4 = dividir \n : "))

if var1 > 4:
    print("\n sinto muito, nao temos essa operacao, por favor indique uma operacao que esteja na lista")


var2 = float(input("\n qual o primeiro valor?:"))

var3 = float(input("\n qual o segundo valor?:"))

if var1 == 1:
    resultado = var2 + var3
    print("\n %a + %a = %a \n \n o resultado da sua soma e %a" %(var2, var3, resultado, resultado))
    
elif var1 == 2:
    resultado = var2 - var3 
    print("\n %a - %a = %a \n \n o resultado da sua subitracao e %a" %(var2, var3, resultado, resultado))

elif var1 == 3:
    resultado = var2 * var3
    print("\n %a * %a = %a \n \n o resultado da sua multiplicacao e %a" %(var2, var3, resultado, resultado))

elif var1 == 4:
    resultado = var2 / var3 
    print("\n %a / %a = %a \n \n o resultado da sua divisao e %a" %(var2, var3, resultado, resultado))

