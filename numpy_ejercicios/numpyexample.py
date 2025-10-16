import numpy as np
# import pandas as pd

# a=np.array([1,2,3])
# print(type[a])
# print(a.shape)
# print(a[2])
# a[0]=100
# a[1]+=1000
# a[2]-=1000
# print(a)

# print("------------------------------------------------------------------------")

# b=np.array([[1,2,3],[1,2,3]])
# print(type[b])
# print(b.shape)
# print(b)

# b[1,2]+=100
# print(b)

# print("------------------------------------------------------------------------")

# a=np.zeros([4,5])
# print(a)
# print(a.shape)

# b=np.ones([2,4])
# print(b)
# print(b.shape)

# c=np.eye(4)
# print(c)

# d=np.full([5,5],8)
# print(d)

# e=np.random.random([3,3])
# print(e)

# print("------------------------------------------------------------------------")
# #matriz aleatoria de 3*4 pero con numeros enteros

# f=np.random.randint(0,10,size=(3,4)) 
# print(f)

# print("------------------------------------------------------------------------")

# g = np.random.randint(1, 20, (5,6))
# print("Matriz g:")
# print(g)
# submatriz_g = g[1:4, 2:5]
# print("\nSubmatriz de g (filas 1-3, columnas 2-4):")
# print(submatriz_g)


# print("------------------------------------------------------------------------")

# a=np.array([[1,2],[3,4],[5,6]])
# print(a)
# print(a.shape)

# filtro=(a>2)
# print(filtro)
# print(a[filtro])

# print("------------------------------------------------------------------------")

# matriz = np.random.randint(1, 100, size=(7, 7))
# print(matriz)
# filtro=(matriz>=40) & (matriz<=60)
# resultado= matriz[filtro]
# print(resultado)

# print("------------------------------------------------------------------------")

# x=np.array([[1,2],[3,4]])
# y=np.array([[10,20],[30,40]])

# print(x)
# print(y)
# print(x.shape)
# print(y.shape)

# #suma inteligente
# print(x+y)
# print(np.add(x,y))
# #multiplicacionde matriz
# print(np.dot(x,y))

# print("------------------------------------------------------------------------")

# g = np.random.randint(11, 100, (3,4))
# print(g)

# print(np.sum(g,axis=0))#fila
# print(np.sum(g,axis=1))#columa
# print(np.sum(g))#todo

# x=np.array([[1,2],[3,4]])
# print(x)
# print(x.T)

print("------------------------------------------------------------------------")
x=np.array([[1,2],[3,4]])
y=np.array([[10,20],[30,40]])

newmatriz=np.vstack((x,y))
print(newmatriz)
print(newmatriz.shape)

newmatriz=np.hstack((x,y))
print(newmatriz)
print(newmatriz.shape)

c=np.concatenate((x,y),axis=0)
print("matriz = \n", c)
print(c.shape)

c=np.concatenate((x,y),axis=0)
print("matriz = \n", c)
print(c.shape)
