#Objetivo mostrar o maior de dois numeros

n1 = int(input("Escreva um numero inteiro: "))
n2 = int(input("Escreva outro numero inteiro: "))

if n1 > n2 :
    maior = n1 
else :
    maior = n2

if maior % 2 == 0 :
     print(f"{maior} é o maior. Ele é par")
else :
     print(f"{maior} é o maior. Ele é impar")

