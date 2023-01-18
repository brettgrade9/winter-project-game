# winter-project-game
This file is a small game where one player moves with "up, down, left, right" and hides with "hide". The second player looks for the hiding spot. To run the game enter "Hide and Seek"\
[![Alternate Text](https://user-images.githubusercontent.com/89731694/212645755-9ef2e462-644a-42f9-8a61-7e1577742d6d.png)](Screen%20Recording%202023-01-16%20at%2012.11.10%20PM.mov "Link Title")
At one point I was stuck and didn't know what to do. This was when I was trying to create the 5 by 5 grid for the player to move around on. I first make an array that was 5 squares.\
"row = ['■', '■', '■', '■', '■']"\
But when I printed the array it showed up like this; ['■', '■', '■', '■', '■']\
So I made a function that typed each letter in the array and repeated 5 times.\
x = 4\
    while i <= x:\
        print(row[i])\
        i += 1\
This took away everything that wasn't a square but printed this;\
■\
■\
■\
■\
■\
But this wasn't what I wanted since I wanted the array to be a row. However, I decided that I could still use this and solve the problem in a different way. So I renamed the array from row to collum and repeated 5 times.\
collum1 = ['■', '■', '■', '■', '■']\
collum2 = ['■', '■', '■', '■', '■']\
collum3 = ['■', '■', '■', '■', '■']\
collum4 = ['■', '■', '■', '■', '■']\
collum5 = ['■', '■', '■', '■', '■']\
    while i <= y:\
        print(collum1[i], collum2[i], collum3[i], collum4[i], collum5[i])\
        i += 1\
This then printed;\
■ ■ ■ ■ ■\
■ ■ ■ ■ ■\
■ ■ ■ ■ ■\
■ ■ ■ ■ ■\
■ ■ ■ ■ ■\
After overcoming this problem I then decided to make a player to move around the grid.\
\
Data abstration is taking data and simplifiying it for the user of the code. I did this is my code by turning the data like the x and y values of the player into positions on the grid. For instance the position of the player is stored in values like playerx and playery.\
playery = 2\
playerx = 2\
And this data is abstractly retrived and converted into a position with this code;\
    if playerx == 0:\
        collum1 = ['■', '■', '■', '■', '■']\
        collum1[playery] = '□'\
    else:\
        collum1[playery] = '■'\
    if playerx == 1:\
        collum2 = ['■', '■', '■', '■', '■']\
        collum2[playery] = '□'\
    else:\
        collum2[playery] = '■'\
    if playerx == 2:\
        collum3 = ['■', '■', '■', '■', '■']\
        collum3[playery] = '□'\
    else:\
        collum3[playery] = '■'\
    if playerx == 3:\
        collum4 = ['■', '■', '■', '■', '■']\
        collum4[playery] = '□'\
    else:\
        collum4[playery] = '■'\
    if playerx == 4:\
        collum5 = ['■', '■', '■', '■', '■']\
        collum5[playery] = '□'\
    else:\
        collum5[playery] = '■'\
This is a single code segement that includes;/
directions = input() <- **Procedure**\
os.system('clear')\
print("■ ■ ■ ■ ■\n■ ■ ■ ■ ■\n■ ■ □ ■ ■\n■ ■ ■ ■ ■\n■ ■ ■ ■ ■\n")\
def hideandseek(): <- **Algorithm**\
    global y, x, playery, playerx, placey, placex, moves, i, gamestate, collum1, collum2, collum3, collum4, collum5\
    directions = input()\
    if (directions == 'up') & (playery > 0):\
        playery -= 1\
        if gamestate == 0:\
            moves += 1\
    if (directions == 'down') & (playery < 4):\
        playery += 1\
        if gamestate == 0:\
            moves += 1\
    if (directions == 'left') & (playerx > 0):\
        playerx -= 1\
        if gamestate == 0:\
            moves += 1\
    if (directions == 'right') & (playerx < 4):\
        playerx += 1 <- **Called Elsewhere in the Program**\
        if gamestate == 0:\
            moves += 1\
    if directions == 'hide':\
        gamestate = 1\
        placey = playery\
        placex = playerx\
        collum1 = ['■', '■', '■', '■', '■']\
        collum2 = ['■', '■', '■', '■', '■']\
        collum3 = ['■', '■', '■', '■', '■']\
        collum4 = ['■', '■', '■', '■', '■']\
        collum5 = ['■', '■', '■', '■', '■']\
        playery = 2 <- **Return a Value**\
        playerx = 2\
Now I will exsplain how the above algorithm functions. First all the variables defined at the beggining of the code are brought into the function. Then I have a variable called 'directions' that changes the values of 'playery' and 'playerx'. If the player types 'hide' then I change the 'gamestate' from 0 to 1. This makes it so the game for the hider is over and it is now the seekers turn. The difference is that the moves aren't counted and the seeker gets a message when it finds the hider. Under this code is where the grid is made and updated. It is done by checking the 'playerx' variable. If it is 0 then the first collum is printed without a black square. Then the 'playery' variable is checked. Finally, the player's black square is printed in the corrosponding white square in the collum varaible. For, example when 'playery' equals 2 then 'collum1[2] = '□'. After, the algorithm checks if the seeker and hider are on the same corodinates. If they are then the code prints the the seeker found the hider. The last thing in the function is the printing of the gride. The five collums which are variables have their individual squares printed on a line which repeats five times to make a square. The purpose of this program is to provide a simple game and to help me understand python better.\
If my program did not have procedural abstraction it would be harder to read the code and require more code. My code can adapt to different situations and be applied to different numbers. For instance, five if statements make twenty five different outcomes and there are only two variables that are put into these if statements.\
    if playerx == 0:\
        collum1 = ['■', '■', '■', '■', '■']\
        collum1[playery] = '□'\
    else:\
        collum1[playery] = '■'\
    if playerx == 1:\
        collum2 = ['■', '■', '■', '■', '■']\
        collum2[playery] = '□'\
    else:\
        collum2[playery] = '■'\
    if playerx == 2:\
        collum3 = ['■', '■', '■', '■', '■']\
        collum3[playery] = '□'\
    else:\
        collum3[playery] = '■'\
    if playerx == 3:\
        collum4 = ['■', '■', '■', '■', '■']\
        collum4[playery] = '□'\
    else:\
        collum4[playery] = '■'\
    if playerx == 4:\
        collum5 = ['■', '■', '■', '■', '■']\
        collum5[playery] = '□'\
    else:\
        collum5[playery] = '■'\
