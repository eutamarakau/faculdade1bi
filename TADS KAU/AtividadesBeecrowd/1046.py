'''
RESOLUÇÃO aTIVIDaDE 1046
24/04/2025

Professor Gregory. aluno(a) Kauane Tamara
'''
#Tempo de jogo

horaInicial, horaFinal = map(int, input("").split())

if (horaInicial < horaFinal): 
    tempo = horaFinal - horaInicial
else:
    tempo = 24 - horaInicial + horaFinal
print(f'O JOGO DUROU {tempo} HORA(S)')
        