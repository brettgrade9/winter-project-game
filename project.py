import time
import os
y = 4
x = 4
playery = 2
playerx = 2
placey = 0
placex = 0
moves = 0
i = 0
gamestate = 0
collum1 = ['■', '■', '■', '■', '■']
collum2 = ['■', '■', '■', '■', '■']
collum3 = ['■', '■', '■', '■', '■']
collum4 = ['■', '■', '■', '■', '■']
collum5 = ['■', '■', '■', '■', '■']
directions = input()
os.system('clear')
print("■ ■ ■ ■ ■\n■ ■ ■ ■ ■\n■ ■ □ ■ ■\n■ ■ ■ ■ ■\n■ ■ ■ ■ ■\n")
def hideandseek():
    global y, x, playery, playerx, placey, placex, moves, i, gamestate, collum1, collum2, collum3, collum4, collum5
    directions = input()
    if (directions == 'up') & (playery > 0):
        playery -= 1
        if gamestate == 0:
            moves += 1
    if (directions == 'down') & (playery < 4):
        playery += 1
        if gamestate == 0:
            moves += 1
    if (directions == 'left') & (playerx > 0):
        playerx -= 1
        if gamestate == 0:
            moves += 1
    if (directions == 'right') & (playerx < 4):
        playerx += 1
        if gamestate == 0:
            moves += 1
    if directions == 'hide':
        gamestate = 1
        placey = playery
        placex = playerx
        collum1 = ['■', '■', '■', '■', '■']
        collum2 = ['■', '■', '■', '■', '■']
        collum3 = ['■', '■', '■', '■', '■']
        collum4 = ['■', '■', '■', '■', '■']
        collum5 = ['■', '■', '■', '■', '■']
        playery = 2
        playerx = 2
    if playerx == 0:
        collum1 = ['■', '■', '■', '■', '■']
        collum1[playery] = '□'
    else:
        collum1[playery] = '■'
    if playerx == 1:
        collum2 = ['■', '■', '■', '■', '■']
        collum2[playery] = '□'
    else:
        collum2[playery] = '■'
    if playerx == 2:
        collum3 = ['■', '■', '■', '■', '■']
        collum3[playery] = '□'
    else:
        collum3[playery] = '■'
    if playerx == 3:
        collum4 = ['■', '■', '■', '■', '■']
        collum4[playery] = '□'
    else:
        collum4[playery] = '■'
    if playerx == 4:
        collum5 = ['■', '■', '■', '■', '■']
        collum5[playery] = '□'
    else:
        collum5[playery] = '■'
    os.system('clear')
    if (playery == placey) & (playerx == placex):
        print("You found the hider")
    else:
        print("The hider moved");print(moves)
    while i <= y:
        print(collum1[i], collum2[i], collum3[i], collum4[i], collum5[i])
        i += 1
    i = 0
while 1 == 1:
        hideandseek()
