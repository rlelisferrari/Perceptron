import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_unweighted, venn2_circles

#A = { x | x é par e 0 < x < 10}
#B = { x | 0 <= x < 10}
#C = { x | x é par}

#listas
listaInteiros = list(range(-100,100))
listaInteirosMenor10 = list(range(0,10))
listaInteirosPares = [x for x in listaInteiros if x % 2 == 0]  

#conjuntos
B = set(listaInteirosMenor10)
C = set(listaInteirosPares)
A = B & C

print("A contido em B: " + str(A < B))
print("A contido em C: " + str(A < C))
print("B contido em C: " + str(B < C))
print("C contido em D: " + str(C < B))

print(B)
print(C)
print(A)

#B - A
quantBnaoA = len(B - A)
quantCnaoA = len(C - A)
quantA = len(A)

legenda = ['B: Inteiros 0 <= x < 10','C: Inteiros Pares']
items = [quantBnaoA,quantCnaoA,quantA]
# venn2(subsets=items,set_labels=legenda,set_colors=('blue','yellow'),alpha=0.7)
venn2_unweighted(subsets=items,set_labels=legenda,set_colors=('blue','yellow'),alpha=0.7)
# venn2_circles(subsets=items)
plt.title('Diagrama de Venn - Conjuntos')
plt.show()