"""3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, 
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).

Примечания:

a. граф должен храниться в виде списка смежности;

b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин."""

num = int(input('Введите количество вершин: '))

g =[[None for i in range(num)] for j in range(num)]

def graph(num):
    for i in range(num):
        for j in range(num):
            if j != i:
                g[i][j] = j

    for row in g:
        for i, vertex in enumerate(row):
            if vertex is None:
                del row[i]
                
    return g

def dfs(g):
    pass

graph(num)


