
'''
import random
m = []
for x in range(1,11):
    MatrizA = []
    for y in range(1, 11):
        MatrizA.append(random.randint(1, 200))
    print(MatrizA)
    m.append(MatrizA)
    print("--- Matriz A ---")
    print(m)
    '''

matriz_a = [[158, 112, 195, 140, 141, 114, 168, 100, 1, 181], [169, 33, 38, 111, 42, 29, 47, 97, 94, 126], [160, 168, 67, 2, 48, 182, 68, 151, 2, 24], [114, 44, 66, 22, 185, 30, 45, 25, 180, 148], [172, 77, 166, 193, 184, 105, 25, 110, 200, 54], [12, 113, 65, 98, 108, 93, 162, 192, 195, 173], [77, 179, 54, 23, 38, 152, 15, 99, 130, 153], [146, 74, 144, 72, 28, 186, 23, 5, 106, 93], [111, 132, 185, 25, 109, 195, 123, 190, 140, 196], [119, 194, 183, 187, 34, 115, 23, 175, 19, 35]]

soma = 0
for i in matriz_a:
    for j in i:
        soma += j
print(f'Somatória = {soma}')

matriz_b = []
for i in range(0, len(matriz_a)):
    lista_auxiliar = []
    for j in range(0, len(matriz_a[i])):
        multiplicacao = matriz_a[i][j] * 3
        lista_auxiliar.append(multiplicacao)
    matriz_b.append(lista_auxiliar)
print(matriz_b)