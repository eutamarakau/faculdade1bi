'''
RESOLUÇÃO ATIVIDADE 1044
10/04/2025

Professor Gregory. Aluno(a) Kauane Tamara
'''
#para numeros na mesma linha
a,b = map(int, input().split(" "))

if a % b == 0 or b % a == 0:
     print("Sao Multiplos")
else :
     print("Nao sao Multiplos")