# importing modules needed 
import random 
import curses

screen = curses.initscr()
curses.curs_set(0)


#get max screen height and width
screen_height, screen_width = screen.getmaxyx()


# create a new window
window = curses.newwin(screen_height, screen_width,0,0)

# allow window to receive input from the keyboard
window.keypad(1)

#  set the delay for updating the screen
window.timeout(100)

# set the x,y coordinates of the snake
snk_x = screen_width // 4
snk_y = screen_height // 2

# the snake's body
snake =[
        [snk_y,snk_x],
        [snk_y,snk_x-1],
        [snk_y,snk_x-2]
   ]

# the food in the middle of the window 
food = [screen_height // 2, screen_width // 2] 

# add the food by using pi char from curses module
window.addch(food[0], food[1], curses.ACS_DIAMOND)

# set intial movement direction to right 
key = curses.KEY_RIGHT

# The loop that will keep running until the player loses or quits the game
while True:
    # Get the next key that will be pressed by the user 
    next_key = window.getch()
    key = key if next_key == -1 else next_key
    
    # Checking if the snake collided with the walls or itself
    if snake[0][0] in [0, screen_height] or snake[0][1] in [0, screen_width] or snake[0] in snake[1:] :
        curses.endwin() # Close window
        quit() # Exit the Game
   
    # set the new pos of the snake head based on the direction        
    new_head = [snake[0][0] , snake[0][1]]    
    
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    
    #insert the new head to the first pos of snake list 
    snake.insert(0, new_head)

    #check if the snake eats
    if snake[0] == food:
        food = None # remove food
        while food is None:
            new_food = [
                        random.randint(1, screen_height-1),
                        random.randint(1, screen_width-1)
                    ]
            food = new_food if new_food not in snake else None
                           
        window.addch(food[0], food[1], curses.ACS_DIAMOND)
    else:
        tail = snake.pop()
        window.addch(tail[0],tail[1], ' ')
    window.addch(snake[0][0], snake[0][1], curses.ACS_BOARD)
    

