# Welcome to the code for cottage-tui!
# The main program will be placed here 
import time 

toDoList = []




#func that shows list to user in fancy format
def showToDo():



#func that runs when user inputs command to insert item into to do list 
def addItem():
    item = input("What would you like to add to the to do list?")
    toDoList.append(item)
    showToDo()


#starts everytime program runs 
def startMenu():
    print("""   __________  _______________   ____________   ________  ______
  / ____/ __ \/_  __/_  __/   | / ____/ ____/  /_  __/ / / /  _/
 / /   / / / / / /   / / / /| |/ / __/ __/      / / / / / // /  
/ /___/ /_/ / / /   / / / ___ / /_/ / /___     / / / /_/ // /   
\____/\____/ /_/   /_/ /_/  |_\____/_____/    /_/  \____/___/   
                                                                """)
    print(" Welcome to Cottage TUI! \n")
    print(" For a list of commands do ctui help")
    print(" To start the timer use the command ctui start {time}")

# timer 
def timer(t):
    
    t = input("Enter the time in seconds: ")
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print('Your timer is up!')


startMenu()

addItem()




