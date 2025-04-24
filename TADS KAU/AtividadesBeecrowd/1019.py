'''
RESOLUÇÃO ATIVIDADE 1019
21/04/2025

Professor Gregory. Aluno(codigo) Kauane Tamara
'''
# Conversão de tempo
segundos = int(input())

horas = segundos//3600
segundos %= 3600
minuts =segundos//60
segundos %= 60

print(f'{horas}:{minuts}:{segundos}')


#print(f'{x//100} nota(s) de R$ 100,00')
#x %=100