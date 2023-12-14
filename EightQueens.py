#
# @author: Jaime Alberto Quiñones
#
# This program gives a solution of the 8-queen problem.
#

import time

class Node:
    def __init__(self, key):
        self.son = []
        self.val = key

def depthSearchQueens(n):
    sol = []
    root = Node(sol)
    stack = [root]

    while stack:
        actual_node = stack[-1]
        actual_vector = actual_node.val.copy()
        stack.pop()

        for i in range(0, n):
            temp_vector = actual_vector.copy()
            temp_vector.append(i)
            if (isPossible(temp_vector.copy(), n)):
                actual_node.son.append(Node(temp_vector))
                stack.append(Node(temp_vector))
                if (len(temp_vector) == n and isSolution(temp_vector)):
                    sol = temp_vector
                    return temp_vector

    return sol


def breadthSearchQueens(n):
    sol = []
    root = Node(sol)
    queue = [root]

    while queue:
        actual_Node = queue[0]
        actual_vector = actual_Node.val.copy()
        queue.pop(0)

        for i in range(0, n):
            temp_vector = actual_vector.copy()
            temp_vector.append(i)
            if isPossible(temp_vector.copy(), n):
                actual_Node.son.append(Node(temp_vector))
                queue.append(Node(temp_vector))
                if len(temp_vector) == n and isSolution(temp_vector):
                    sol = temp_vector
                    return temp_vector
                
    return sol


def isPossible(vector, n):
    if len(vector) <= 1:
        return True
    else:
        pos_row = len(vector) - 1
        pos_col = vector.pop()
        actual_row = 0
        for actual_col in vector:
            if actual_col == pos_col:
                return False
            i, j = actual_row + 1, actual_col + 1
            while i < n and j < n:
                if i == pos_row and j == pos_col:
                    return False
                i += 1
                j += 1
            i, j = actual_row + 1, actual_col - 1
            while i < n and j >= 0:
                if i == pos_row and j == pos_col:
                    return False
                i += 1
                j -= 1
            actual_row = actual_row + 1
        return True



def isSolution(vector):
    for i in vector:
        for j in range(i + 1, len(vector)):
            if (i == j):
                return False
    return True


ini = time.time()
print(depthSearchQueens(16))
end = time.time()
print(end - ini)

'''
ini_2 = time.time()
print(breadthSearchQueens(8))
end_2 = time.time()
print(end_2 - ini_2)
'''