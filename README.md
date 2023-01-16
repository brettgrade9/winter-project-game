# winter-project-game
This file is a small game where one player moves with "up, down, left, right" and hides with "hide". The second player looks for the hiding spot. To run the game enter "Hide and Seek"
[![Alternate Text](https://user-images.githubusercontent.com/89731694/212645755-9ef2e462-644a-42f9-8a61-7e1577742d6d.png)](Screen%20Recording%202023-01-16%20at%2012.11.10%20PM.mov "Link Title")
At one point I was stuck and didn't know what to do. This was when I was trying to create the 5 by 5 grid for the player to move around on. I first make an array that was 5 squares.
"row = ['■', '■', '■', '■', '■']"
But when I printed the array it showed up like this; ['■', '■', '■', '■', '■']
So I made a function that typed each letter in the array and repeated 5 times.
x = 4
    while i <= x:
        print(row[i])
        i += 1
This took away everything that wasn't a square but printed this;
■
■
■
■
■
But this wasn't what I wanted since I wanted the array to be a row. However, I decided that I could still use this and solve the problem in a different way. So I renamed the array from row to collum and repeated 5 times.
collum1 = ['■', '■', '■', '■', '■']
collum2 = ['■', '■', '■', '■', '■']
collum3 = ['■', '■', '■', '■', '■']
collum4 = ['■', '■', '■', '■', '■']
collum5 = ['■', '■', '■', '■', '■']
    while i <= y:
        print(collum1[i], collum2[i], collum3[i], collum4[i], collum5[i])
        i += 1
This then printed;
■ ■ ■ ■ ■
■ ■ ■ ■ ■
■ ■ ■ ■ ■
■ ■ ■ ■ ■
■ ■ ■ ■ ■
After overcoming this problem I then decided to make a player to move around the grid.

Data abstration is taking data and simplifiying it for the user of the code. I did this is my code by turning the data like the x and y values of the player into positions on the grid. For instance the position of the player is stored in values like playerx and playery.
playery = 2
playerx = 2
And this data is abstractly retrived and converted into a position with this code;
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
