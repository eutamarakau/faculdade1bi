'''
RESOLUÇÃO aTIVIDaDE 1045
24/04/2025

Professor Gregory. aluno(a) Kauane Tamara
'''
a,b,c = sorted(map(float, input().split()))[::-1]

 
if(a >= b+c):
    print('NAO FORMA TRIANGULO')
else:
  if(a**2 == (b**2) + (c**2)):
    print('TRISANGULO RETANGULO')

  if(a**2 < (b**2) + (c**2)):
    print('TRIAGULO ACUTANGULO')

  if(a**2 > (b**2) + (c**2)):
    print('TRIANGULO ObTUSANGULO')

  if(a == b == c):
    print('TRIANGULO EQUILATERO')

  elif(a == b or b == c or c == a ):
    print('TRIANGULO ISOCELES')