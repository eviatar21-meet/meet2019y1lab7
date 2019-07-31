import turtle
import random
import time

turtle.tracer(1,0) 

turtle.bgcolor('violet')

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y)

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6
TIME_STEP = 100

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

turtle.register_shape("ssszach.gif")
snake = turtle.clone()
snake.shape("circle")
def zach():
    snake.shape("ssszach.gif")
def circle():
    snake.shape("circle")
def square():
    snake.shape("square")

turtle.hideturtle()

#draws a part of the snake on the screen

def new_stamp():
    snake_pos = snake.pos()
    pos_list.append(snake_pos) 
    snake_stamp = snake.stamp()
    stamp_list.append(snake_stamp)



for i  in range(START_LENGTH) :
    x_pos=snake.pos()[0] 
    y_pos=snake.pos()[1] 
    x_pos+=SQUARE_SIZE 

    snake.goto(x_pos,y_pos) 
    new_stamp()

def remove_tail():
    old_stamp = stamp_list.pop(0) 
    snake.clearstamp(old_stamp) 
    pos_list.pop(0)

snake.direction = "Up"

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400


def up():
    snake.direction="Up"  
    print("You pressed the up key!")
def down():
    snake.direction="down"  
    print("You pressed the down key!")
def left():
    snake.direction="left"  
    print("You pressed the left key!")
def right():
    snake.direction="right"  
    print("You pressed the right key!")



turtle.onkeypress(up, "Up") 
turtle.onkeypress(down, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.onkeypress(circle, "1")
turtle.onkeypress(square, "2")
turtle.onkeypress(zach, "3")




turtle.listen()
turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif") 

food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

for this_food_pos in food_pos:
    food.goto(this_food_pos)
    food_stamp = food.stamp()
    food_stamps.append(food_stamp)
    food.hideturtle()
    
def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    
    food.goto(food_x,food_y)
    food_pos.append(food.pos())
    food_stamp = food.stamp()
    food_stamps.append(food_stamp)

    
def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    
    turtle.clear()
    turtle.write(len(stamp_list),font=("ariel",40,"bold"))
    
    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)

    elif snake.direction=="down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
    elif snake.direction=="right":
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
    elif snake.direction=="left":
        snake.goto(x_pos - SQUARE_SIZE, y_pos)

    
    new_stamp()

    if snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos()) 
        food.clearstamp(food_stamps[food_index]) 
        food_pos.pop(food_index) 
        food_stamps.pop(food_index)
        new_stamp()
        print("You have eaten the food!")
        colors= ('blue','red','orange','green','yellow','black','Lavender')
    
        rancolor=colors[random.randint(0,6)]
        turtle.bgcolor(rancolor)
    
    

    elif snake.pos() in pos_list[0:-1]:
        print("You hit yourself! Game over!")
        quit()
    
    remove_tail()

    
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    
    if new_x_pos >= RIGHT_EDGE:
         print("You hit the right edge! Game over!")
         quit()
    if new_x_pos <= LEFT_EDGE:
         print("You hit the left edge! Game over!")
         quit()
    if new_y_pos >= UP_EDGE:
         print("You hit the top edge! Game over!")
         quit()
    if new_y_pos <= DOWN_EDGE:
         print("You hit the bottom edge! Game over!")
         quit()

    if len(food_stamps) <= 3 :
        make_food()


    turtle.ontimer(move_snake,TIME_STEP)

move_snake()





turtle.mainloop()


