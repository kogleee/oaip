lab = [
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
 [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
 [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
 [1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
 [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
 [1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
 [1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
 [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


def BFS(start, end, lab):
    current = start # текущее положение
    visited = [start] # посещённые
    stack =[] # очередь

    #поиск соседних элементов с текущим положением
    while end not in visited:
        for i in range(current[0] - 1, current[0] + 2):
            for j in range(current[1] - 1, current[1] + 2):
                if lab[i][j] == 0:
                    if ([i,j] not in stack) and ([i,j] not in visited):
                        stack.append([i,j])

        #переход на первый элемент в очереди, добавление в посещённые и удаление из очереди
        current = stack[0]
        visited.append(stack[0])
        stack.remove(stack[0])
        print(current)

BFS([1,3],[8,1], lab)

























