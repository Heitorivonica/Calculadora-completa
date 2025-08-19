def soma(a, b): #defindo a função soma
    return (a + b ) 

def subtração(a , b): #definindo a função subtração
    return(a - b)
def multiplicação(a, b): #definindo a função multiplicação
    return(a * b)
def divisão(a, b):  #definindo a função divisão
    if b == 0:   #se caso o b for igual a zero o codigo ira retonar um erro
        return None
    else: 
     return(a / b)
def potenciação(a, b):  #definindo a função potenciação
    return(a ** b)
def raiz_quadrada(a): #definindo a função raiz quadrada
    if a < 0:  # se o valor for menor que zero o codigo ira retornar um erro de raiz negativa
        return None
    else:
        return(a ** 0.5)
while True: # inicia o loop para a calculadora
 print("bem vindo a calculadora")
 print("\nescolha uma operação:")
 print("a - soma")
 print("b - subtração")
 print("c - multiplicação")
 print("d - divisão")
 print("e - potenciação")
 print("f - raiz_quadrada")
 print( " s - sair") # opção para sair da calculadora/loop 


 escolha = input("digite a opção desejada:") # lower() transforma tudo em minusculo 
 if escolha == "s": # escolha igual a s o loop ira parar
    print(" fechando a calculadora até mais!")
    break # caso o usuario escolha a opção s o loop ira parar e o programa ira voltar para parte de opções da calculadora
 


 if escolha == "a": 
    a = float(input(" digite o primeiro numero:"))
    b = float(input(" digite o segundo  numero:"))
    print("resultado:", soma(a, b))  # imprime o resultado da soma 

 elif escolha == "b":
    a = float(input("digite o primeiro numero:"))
    b = float(input("digite o segundo numero:"))
    print("resultado:", subtração(a, b)) # imprime o resultado da subtração 

 elif escolha == "c":
    a = float(input("digite o primeiro numero:"))
    b = float(input("digite o segundo numero: "))
    print("resultado:", multiplicação(a, b)) # imprime o resultado da multiplicação

 elif escolha == "d":
    a = float(input("digite o primeiro numero:"))
    b = float(input("digite o segundo numero:"))
    print("resultado:", divisão(a, b))  #imprime o resultado da divisão

 elif escolha == "e":
    a = float(input("digite o primeiro numero:"))
    b = float(input("digite o segundo numero: "))
    print(" resultado: ", potenciação(a, b)) # imprime o resultado da potenciação 

 elif escolha == "f":
    a = float( input("digite o  primeiro numero:"))
    print("resultado:", raiz_quadrada(a)) # imprime o resultado da raiz quadrada

 
 else: print("opção invalidada tente novamente") # se a opção não for valida o codigo ira imprimir essa mensagem e pedira para o usuario colocar uma opção valida


