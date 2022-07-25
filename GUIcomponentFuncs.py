import sys, pygame, time
pygame.init();

def GUIcompFcn(width, height, x, y, gradient, colour, screen, direction, border, borderCol, borderThick, blit):
    #converting some varaibles into integers incase of user error in calling function
    ratio = height/width;
    width = round(width);
    height = round(height);

    #creating rectangle on screen and returning surface object handle
    block = pygame.surface.Surface((width, height)); #create a surface of width by height pixels

    #creating rectangle on the whole surface created
    if gradient == True and direction == 1:
        for i in range(width):
            for j in range(height):
                firCol = 160*(2*height-(ratio*i)-j)/(2*height);
                secCol = 255*(height-abs(height-(ratio*i)-j))/(2*height);
                thirCol = 160*((ratio*i)+j)/(2*height);
                col = (firCol, secCol, thirCol);
                pygame.draw.rect(block, (col[colour[0] - 1], col[colour[1] - 1], col[colour[2] - 1]), (i, j, 1, 1));
    elif gradient == True and direction == -1:
        for i in range(width):
            for j in range(height):
                firCol = 160*(2*height-(ratio*i)-j)/(2*height);
                secCol = 255*(height-abs(height-(ratio*i)-j))/(2*height);
                thirCol = 160*((ratio*i)+j)/(2*height);
                col = (firCol, secCol, thirCol);
                pygame.draw.rect(block, (col[colour[0] - 1], col[colour[1] - 1], col[colour[2] - 1]), (i, j, 1, 1));
    elif gradient == False:
            pygame.draw.rect(block, colour, (0, 0, width, height)); #add rectangle over whole surface and set colour

    #adding border to object if specified
    if border == 1:
        pygame.draw.rect(block, borderCol, (0, 0, width, height), borderThick);

    #checking if user wants current surface object blited onto screen
    if blit == True:
        screen.blit(block, (x, y)); #adding block surface onto the screen at (x, y)

    #returning the handle to the created component
    return block;
