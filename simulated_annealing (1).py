# -*- coding: utf-8 -*-
"""Simulated_Annealing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L5HsLUc2rMj6xFansRcn5jLsbVw9Kh1p
"""

import copy
import math
import random

SIZE = 3
TEMPERATURE = 1000
COOLING_RATE = 0.95


def calculateHeuristic(state, goal):
    count = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if state[i][j] != goal[i][j]:
                count += 1
    return count


def generateNeighborState(state):
    neighborState = copy.deepcopy(state)
    i, j = findEmptySpace(neighborState)

    while True:
        randomDirection = random.choice(['up', 'down', 'left', 'right'])
        if randomDirection == 'up' and i > 0:
            neighborState[i][j], neighborState[i - 1][j] = neighborState[i - 1][j], neighborState[i][j]
            break
        elif randomDirection == 'down' and i < SIZE - 1:
            neighborState[i][j], neighborState[i + 1][j] = neighborState[i + 1][j], neighborState[i][j]
            break
        elif randomDirection == 'left' and j > 0:
            neighborState[i][j], neighborState[i][j - 1] = neighborState[i][j - 1], neighborState[i][j]
            break
        elif randomDirection == 'right' and j < SIZE - 1:
            neighborState[i][j], neighborState[i][j + 1] = neighborState[i][j + 1], neighborState[i][j]
            break

    return neighborState


def findEmptySpace(state):
    for i in range(SIZE):
        for j in range(SIZE):
            if state[i][j] == 0:
                return i, j


def simulatedAnnealingSearch(initialState, goal):
    currentState = copy.deepcopy(initialState)
    currentHeuristic = calculateHeuristic(currentState, goal)
    bestState = copy.deepcopy(currentState)
    bestHeuristic = currentHeuristic

    temperature = TEMPERATURE

    while temperature > 0:
        neighborState = generateNeighborState(currentState)
        neighborHeuristic = calculateHeuristic(neighborState, goal)

        deltaE = neighborHeuristic - currentHeuristic

        if deltaE < 0 or math.exp(-deltaE / temperature) > random.random():
            currentState = copy.deepcopy(neighborState)
            currentHeuristic = neighborHeuristic

        if currentHeuristic < bestHeuristic:
            bestState = copy.deepcopy(currentState)
            bestHeuristic = currentHeuristic

        temperature *= COOLING_RATE


    print("Final State:")
    for row in bestState:
        print(row)


initialState = [
    [3, 2, 4],
    [8, 1, 5],
    [0, 6, 7]
]
goalState = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

simulatedAnnealingSearch(initialState, goalState)