#This Code was written by Husam Abu-Gharbieh.
#Email: abugharbieh.h@gmail.com
#Date: 11th of August 2012.

import pygame
import math
 
# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
blue =(0, 0, 255)

dPlayer = 1
dPlayer_one_score = 0
dPlayer_two_score = 0

winner = ""
bDone = False #Done one game.

aBoard = ['z','z','z','z','z','z','z','z','z']
aPositions = [ [100,50], [150,50], [200,50], [100,100], [150,100], [200,100], [100,150], [150,150], [200,150]] #for drawing.

def add_text(sText, aColor, aCoordinates):
    font = pygame.font.Font(None, 25)
    text = font.render(sText,True,aColor)
    screen.blit(text, aCoordinates)
    
def draw_game():
    pygame.draw.line(screen,black,[150,50],[150,210],5)
    pygame.draw.line(screen,black,[200,50],[200,210],5)
    pygame.draw.line(screen,black,[100,100],[250,100],5)
    pygame.draw.line(screen,black,[100,150],[250,150],5)

def draw_score():
    add_text("Score",green,[150,220])
    
    add_text("Player: 1",green,[80,250])
    
    add_text("Player: 2",green,[200,250])
    
    add_text(str(dPlayer_one_score),green,[115,270])
    
    add_text(str(dPlayer_two_score),green,[235,270])    


def draw_X(dPos):
    dStart = aPositions[dPos]
    
    pygame.draw.line(screen,red,[dStart[0] + 5,dStart[1] + 5],[dStart[0] + 45,dStart[1] + 45],2)
    pygame.draw.line(screen,red,[dStart[0] + 45,dStart[1] + 5],[dStart[0] + 5,dStart[1] + 45],2)
    
def draw_O(dPos):
    dStart = aPositions[dPos]
    
    pygame.draw.ellipse(screen,blue,[dStart[0] + 5,dStart[1] + 5,45,45],2)

def add_to_board(x_co,y_co,dPos,min_x,min_y):
    global dPlayer
    if x_co > min_x and x_co < (min_x + 50) and y_co > min_y and y_co < (min_y + 50) and  aBoard[int(dPos)-1] == 'z':
        if dPlayer == 1:
           aBoard[int(dPos)-1] = 'x'
        else:
            aBoard[int(dPos)-1] = 'o'
        
        dPlayer = (dPlayer % 2) + 1 # to keep it between 1 and 2
        
    
def action(dPlayer,coordinates):
    if bDone == True:
        return
    x_co = coordinates[0]
    y_co = coordinates[1]
    
    #Check if out of the game range.
    if x_co < 100 or x_co > 250 or y_co < 50 or y_co > 200:
        return
    
    x_pos = x_co - 100
    x_pos = math.ceil(x_pos / 50.0)
    
    y_pos = y_co - 50
    y_pos = math.ceil(y_pos / 50.0)

    #blocks of the board are noted by 1..2...3.....9
    dPos = x_pos + ((y_pos - 1) * 3)
    
    min_x = (x_pos+1) * 50
    min_y = y_pos * 50
    
    add_to_board(x_co,y_co,dPos,min_x,min_y)
            

def clear_game():
    global winner
    if winner == 'x':
            global dPlayer_one_score
            dPlayer_one_score = dPlayer_one_score + 1
    elif winner == 'o':
            global dPlayer_two_score
            dPlayer_two_score = dPlayer_two_score + 1
            
    global aBoard
    aBoard = ['z','z','z','z','z','z','z','z','z']
    global bDone
    bDone = False

def check_winner_state(dNode,dNode_two,dNode_three,aStart_line,aEnd_line):
    global bDone
    global winner
    
    if aBoard[dNode] == aBoard[dNode_two] and aBoard[dNode] == aBoard[dNode_three] and aBoard[dNode] != 'z':
        winner = aBoard[dNode]
        pygame.draw.line(screen,green,aStart_line,aEnd_line,5)
        bDone = True
        return True
    return False

def check_game():
    global bDone
    global winner

    if check_winner_state(0,1,2,[115,75],[250,75]):
        pass
    elif check_winner_state(1,4,7,[175,55],[175,200]):
        pass
    elif check_winner_state(0,3,6,[125,55],[125,200]):
        pass
    elif check_winner_state(2,5,8,[225,55],[225,200]):
        pass
    elif check_winner_state(3,4,5,[115,125],[250,125]):
        pass
    elif check_winner_state(6,7,8,[115,175],[250,175]):
        pass
    elif check_winner_state(2,4,6,[250,65],[115,185]):
        pass
    elif check_winner_state(0,4,8,[115,65],[225,180]):
        pass
    elif not 'z' in aBoard:
        winner='draw'
        bDone=True
    
    if bDone == True:
        if winner == 'x':
            sResult = "Player one wins!"
            x_co = 115
        elif winner == 'o':
            sResult = "Player two wins!"
            x_co = 115
        else:
            sResult = "Draw!"
            x_co = 165
        
        
        add_text(str(sResult),green,[x_co,300])
        
        add_text("Click anywhere to continue!",green,[80,320])
            
    return
    
pygame.init()


  
# Set the width and height of the screen [width,height]
size=[360,360]
screen=pygame.display.set_mode(size)
 
pygame.display.set_caption("Tic Tac Toe")
 
#Loop until the user clicks the close button.
done=False
 
# Used to manage how fast the screen updates
clock=pygame.time.Clock()
 
# -------- Main Program Loop -----------
while done==False:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            action(dPlayer,pygame.mouse.get_pos())
            if bDone == True:
                clear_game()
            
            
            
    screen.fill(white)        
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
  
  
    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
    check_game()
 

    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
    
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT    
    
    draw_game()
    
    counter = 0
    for item in aBoard:
        if item == 'x':
            draw_X(counter)
        elif item == 'o':
            draw_O(counter)
        counter = counter + 1
    
    #Player's turn
    add_text("Player: "+str(dPlayer),green,[135,25])    
    
    #Players score
    
    draw_score()
    
    #end of players score
    
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
     
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 20 frames per second
    clock.tick(20)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()
