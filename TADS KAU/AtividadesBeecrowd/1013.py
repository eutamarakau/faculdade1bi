'''
RESOLUÇÃO ATIVIDADE 1013
21/04/2025

Professor Gregory. Aluno(a) Kauane Tamara
'''
# o Maior

a,b,c = (int(x) for x in input().split(" "))

maior=a

if b > maior:
    maior = b

if c > maior:
    maior = c 

print(f'{maior} eh o maior')


