'''
RESOLUÇÃO ATIVIDADE 1038
17/04/2025

Professor Gregory. Aluno(codigo) Kauane Tamara
'''
# Lanche
#x = int(input(" "))

# codigo = codigo
# preco = preco
# c = quantidade

codigo, quantidade= map(int, input("").split())

if codigo == 1:
 preco = 4.00

elif codigo == 2:
 preco = 4.50
 
elif codigo == 3:
 preco = 5.00
 
elif codigo == 4:
 preco = 2.00

elif codigo == 5:
 preco = 1.50

total = quantidade * preco

print("Total: R$ {:.2f}".format(total))
