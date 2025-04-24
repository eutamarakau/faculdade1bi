'''
RESOLUÇÃO ATIVIDADE 1012
17/04/2025

Professor Gregory. Aluno(a) Kauane Tamara
'''
# Área
a,b,c = (float(x) for x in input().split(" "))
π = 3.14159

#a) a área do triângulo retângulo que tem A por base e C por altura.
triangulo = (a * c)/ 2

#b) a área do círculo de raio C.
circulo = π * (c**2)

#c) a área do trapézio que tem A e B por bases e C por altura.
trapezio = (a + b)/2 * c

#d) a área do quadrado que tem lado B.
quadrado = b * b 

#e) a área do retângulo que tem lados A e B.
retangulo = a * b

print ('TRIANGULO: = {:.3f}'.format(triangulo))
print ('CIRCULO: = {:.3f}'.format(circulo))
print ('TRAPEZIO = {:.3f}'.format(trapezio))
print ('QUADRADO: = {:.3f}'.format(quadrado))
print ('RETANGULO: = {:.3f}'.format(retangulo))

