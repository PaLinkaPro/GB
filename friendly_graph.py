"""1. На улице встретились N друзей. 
Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?"""

n = input("Введите число друзей: ")

matrix = [[0 for i in range(int(n))] for j in range(int(n))]

counter = 0

for i, row in enumerate(matrix):
    for j, column in enumerate(row):
        if i != j:
            matrix[i][j] = 1
            counter += 1
#print(*matrix, sep='\n')

print('Было cделано рукопожатий: {} '.format(int(counter / 2)))
