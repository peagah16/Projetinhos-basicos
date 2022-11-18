#funções da calculadora simples
def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n" )

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def mult(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

#Menu da calculadora
while True:
    print("A. Adicao")
    print("B. Subtracao")
    print("C. Multiplicacao")
    print("D. Divisao")
    print("E. Sair")

    choice = input("Insira sua opcao: ")
#condições 
    if choice == "a" or choice == "A":
        print("Adicao")
        a = int(input("Insira o primeiro numero: "))
        b = int(input("Insira o segundo numero: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtracao")
        a = int(input("Insira o primeiro numero: "))
        b = int(input("insira o segundo numero: "))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Multiplicacao")
        a = int(input("Insira o primeiro numero: "))
        b = int(input("insira o segundo numero: "))
        mult(a, b)
    elif choice == "d" or choice == "D":
        print("Divisao")
        a = int(input("Insira o primeiro numero: "))
        b = int(input("insira o segundo numero: "))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("Fechando Programa")
        quit()
    