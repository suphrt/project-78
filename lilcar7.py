#!usr/bin/env python 3
# -*- coding: utf-8 -*-

XAXIS = "ABCDEFGHIJKLMNO"
YAXIS = "12345678"

FORBIDDEN = {"B1", "B2", "B3", "B4", "B5", "B6", "B7",
             "D2", "D3", "D4", "D5", "D6", "D7", "D8",
             "F1", "F2", "F3", "F4", "F5",
             "H1", "H2", "H4", "H5", "H6", "H7", "H3",
             "I3", "I7", "J5", "L1",
             "K2", "K3", "K4", "K5", "K6", "K7", "K8",
             "N2", "N3", "N4", "N5", "N6", "N7", "N8"}

def move(position, direction):
    i = XAXIS.index(position[0])
    j = YAXIS.index(position[1])

    if direction == "left":
        if i > 0:
            return XAXIS[i-1] + position[1]
    elif direction == "right":
        if i < len(XAXIS) - 1:
            return XAXIS[i+1] + position[1]
    elif direction == "up":
        if j > 0:
            return position[0] + YAXIS[j-1]
    elif direction == "down":
        if j < len(YAXIS) - 1:
            return position[0] + YAXIS[j+1]

def can_move(position, direction):
    if direction == "left" and position[0] == XAXIS[0]:
        return False
    elif direction == "right" and position[0] == XAXIS[-1]:
        return False
    elif direction == "up" and position[0] == YAXIS[0]:
        return False
    elif direction == "down" and position[0] == YAXIS[-1]:
        return False

    new_position = move(position, direction)
    return new_position not in FORBIDDEN

def execute(start):
    position = start

    while can_move(position, "down"):
        position = move(position, "down")
    while can_move(position, "left"):
        position = move(position, "left")
    if can_move(position, "up"):
        position = move(position, "up")
    else:
        return False
    if can_move(position, "right"):
        return True
    else:
        return False

if __name__ == '__main__':
    res = 0
    for x in XAXIS:
        for y in YAXIS:
            position = x + y
            if position in FORBIDDEN:
                continue
            if execute(position):
                res +=1
    print(res)

