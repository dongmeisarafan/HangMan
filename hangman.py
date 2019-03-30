#Guin Feldman and Dong Mei Sarafan
#Final Project: Hangman Game
#Due Date: May 18, 2016
#This program is a hangman game. To play the game, the player chooses a level and then types in different letters to try to guess the word.
#If the player is on the easy level, he or she has 1 mintute to guess the word and can only guess 9 wrong letters.
#On the medium level, the player has 45 seconds to guess the word and can only have 5 wrong guesses.
#Finally, on the hard level, the player has 30 seconds and can only have 3 wrong guesses.
#The program uses audio sound every time the player guesses a letter, which will tell the player if he or she guessed a correct letter or not.
#To win the game, the player must guess the word before time is up and the hangman is completely drawn. Otherwise, the player loses.

from graphics import *
from buttonclass import Button
from HangmanClass import *
import time 

#This function is used to create the structure of the hangman. It takes the graphics window as a parameter.
def drawhangman(win):
    #This uses the line object to create each part of the hangman structure.
    pole = Line(Point(6,10),Point(6,18))
    pole.draw(win)
    head = Line(Point(6,18),Point(9,18))
    head.draw(win)
    floor = Line(Point(5,10), Point(10,10))
    floor.draw(win)
    string = Line(Point(9, 18), Point(9, 17))
    string.draw(win)

#This function is used to create the animation in the beginning.
def startimage(win):
    #This function uses the line object to create the structure of the hangman.
    #This is an empty list that holds each object created.
    hangmanset = []
    pole = Line(Point(6,5), Point(6,15))
    pole.draw(win)
    hangmanset.append(pole)
    head = Line(Point(6,15), Point(11,15))
    head.draw(win)
    hangmanset.append(head)
    floor = Line(Point(4,5), Point(11, 5))
    floor.draw(win)
    hangmanset.append(floor)
    string = Line(Point(11,15), Point(11,13))
    string.draw(win)
    hangmanset.append(string)

    #These statements use the circle and line objects to create the man for the hangman.
    #This is an empty list that holds each part of the hangman.
    bodyparts = []   
    bodyhead = Circle(Point(11,25),1)
    bodyhead.draw(win)
    bodyparts.append(bodyhead)
    body = Line(Point(11,21), Point(11,24))
    body.draw(win)
    bodyparts.append(body)
    bodyleg1 = Line(Point(11,21), Point(10,20))
    bodyleg1.draw(win)
    bodyparts.append(bodyleg1)
    bodyleg2 = Line(Point(11,21), Point(12,20))
    bodyleg2.draw(win)
    bodyparts.append(bodyleg2)
    arm1 = Line(Point(11,23), Point(10,24))
    arm1.draw(win)
    bodyparts.append(arm1)
    arm2 = Line(Point(11,23), Point(12,24))
    arm2.draw(win)
    bodyparts.append(arm2)

    #This for loop will run 13 times and is used to make the hangman man move.
    for i in range(13):
        #Each part of the hangman will move down one pixel 13 times.
        bodyhead.move(0,-1)
        body.move(0,-1)
        bodyleg1.move(0,-1)
        bodyleg2.move(0,-1)
        arm1.move(0,-1)
        arm2.move(0,-1)
        #This uses the sleep function to slow down the movement of the objects
        sleep(0.1)
    #These for loops goes through the hangmanset and the bodyparts lists and undraw each object so that the image disappears.
    for part in hangmanset:
        part.undraw()
    for part in bodyparts:
        part.undraw()

def main():
    #Creates a graphics window
    win = GraphWin('Hangman', 800,600)
    win.setBackground('lightblue')
    win.setCoords(-2,-2,20,20)

    #calls the animation at the beginning of the program.
    startimage(win)
    
    #intro text for the user.
    intro = Text(Point(10,15), 'Want to Play Hangman?')
    intro.setSize(36)
    intro.setFill('black')
    intro.draw(win)

    #This uses a text object to display the instructions for the player.
    instru = Text(Point(10,10), 'How to Play:\n Pick a level and then the program will generate a word for you to guess.\n  Depending on the level, you are given a certain number of tries as well as a time limit.\n For the easy level, you can have 9 wrong guesses and 1 minute to guess the word.\n For the medium level you can have 5 wrong guesses and 45 seconds.\n And for the hard level you can have 3 wrong guesses and 30 seconds to guess the word.\n If you succeed in guessing all the letters in the word before your guesses\n or time runs out, you win however, if you fail to guess\n the correct letters or time runs out, you lose')
    instru.draw(win)

    #This uses the image function to display a thought bubble at the beginning of the program.
    bubble = Image(Point(10,10), 'thought-bubbles.png')
    bubble.draw(win)

    #This uses a text object to tell the player to click to continue.
    cont = Text(Point(10,7),'(Click to continue)')
    cont.setSize(10)
    cont.draw(win)

    #click to continue
    pt = win.getMouse()

    #undraw items:
    intro.undraw()
    instru.undraw()
    cont.undraw()
    bubble.undraw()

    #This uses a text object to tell the player to pick a level of difficulty.
    intro2 = Text(Point(10,4), 'Pick a level of difficulty:')
    intro2.setSize(20)
    intro2.draw(win)

    #These statemetns use the button class to create five buttons.
    easyBtn = Button(win,Point(6,2), 3,1, 'Easy')
    mediumBtn = Button(win,Point(10,2), 3,1, 'Medium')
    hardBtn = Button(win,Point(14,2),3,1, 'Hard')
    quitBtn = Button(win,Point(0,19),2,1, 'Quit')
    newBtn = Button(win,Point(18,19),3,1, 'New Game')

    #Entry box
    guess = Entry(Point(15,15), 4)

    #Empty text object that will be used later.
    text = Text(Point(10,1),'')
    text.setSize(15)
    text.draw(win)

    #Empty text that will be used as a reminder to tell the player how many guesses and how much time he or she has.
    text2 = Text(Point(3,15), '')
    text2.setSize(10)
    text2.setFill('purple')
    text2.draw(win)

    
    #Text object that states the letters the player has guessed.
    guesstext = Text(Point(15,11), "Letters Guessed:")
    guesstext.setSize(15)

    #mouse click and calls the hangman class.
    pt= win.getMouse()
    game = Hangman(win)

    #variable for level of difficulty we are on
    state = 0
    #An empty text object that will display the letters guessed.
    entryletter = Text(Point(15, 10), "")
    entryletter.draw(win)

    #Boolean statement to determine whether the game is over.
    end = False

    #This while loop will run while the quit button is not clicked and the game is not over.
    while not quitBtn.clicked(pt) and not end:
        #this calls the losegame method from the hangman class. This statement will run if the game is over and the player lost.
        if game.losegame() == True:
            end = True
        #This calls the wingame method of the hangman class. It will run if the player wins and the game is over.
        if game.wingame() == True:
            end = True
        #This runs if the easy level button is clicked.
        if easyBtn.clicked(pt):
            #We got the time function from Professor Lee.
            #This says that the game will end after 1 minute.
            win.after(60000, game.clock)
            #deactivate buttons and create the guess button.
            easyBtn.deactivate()
            mediumBtn.deactivate()
            hardBtn.deactivate()
            intro2.undraw()
            guessBtn = Button(win,Point(15,17),3,1, 'Guess')
            guess.draw(win)

            #Calls the hangman function to draw the hangman structure.
            drawhangman(win)
            
            #These two statements call methods from the hangman class to read the text file and create blank lines for the word to be displayed on.
            game.difficulty("Easywordlist.txt")
            game.blankword()

            #Text objects to tell the player what level they are on and how many wrong guesses and how much time he or she has.
            text.setText('You are playing an easy level')
            text2.setText('Remember:\n You only have 1 minute \n and 9 wrong guesses!')
            guesstext.draw(win)

            #Variable for the easy level.
            state = 1

        #If the player is on the easy level and presses guess.
        #This condition takes the guess from the entry box and calls the getguess method from the hangman class.
        #These methods either draw the correct letter in the window or draw a part of the hangman.
        if state ==1 and guessBtn.clicked(pt):
            letter = guess.getText().lower()
            correct = game.getGuess(letter, entryletter)
            if correct == False:
                game.hangmanparts()
                game.drawhangman(state)
      
            
        #This is for the medium level.             
        elif mediumBtn.clicked(pt):
            #The game will end after 45 seconds.
            win.after(45000, game.clock)
            #deactivate buttons and create new ones.
            easyBtn.deactivate()
            mediumBtn.deactivate()
            hardBtn.deactivate()
            intro2.undraw()
            guessBtn = Button(win,Point(15,17),3,1, 'Guess')
            guess.draw(win)

            #draw hangman structure
            drawhangman(win)
            #Calls methods from the hangman class to read the text file and create the blank lines.
            game.difficulty("Mediumwordlist.txt")
            game.blankword()
            #Text objects, same as the ones for the easy level.
            text.setText('You are playing a medium level')
            text2.setText('Remember:\n You only have 45 seconds \n and 5 wrong guesses!')
            guesstext.draw(win)

            #Variable for the medium level.
            state = 2

        #This condition will run if the player is on the medium level and clicks the guess button.
        #The methods either draw the correct letter in the window or draw a part of the hangman.
        if state ==2 and guessBtn.clicked(pt):
            letter = guess.getText().lower()
            correct = game.getGuess(letter, entryletter)
            if correct == False:
                game.hangmanparts()
                game.drawhangman(state)
            
        #This is for the hard level.           
        elif hardBtn.clicked(pt):
            #The program will end after 30 seconds.
            win.after(30000, game.clock)
            #Deactivate buttons and create the guess button.
            easyBtn.deactivate()
            mediumBtn.deactivate()
            hardBtn.deactivate()
            intro2.undraw()
            guessBtn = Button(win,Point(15,17),3,1, 'Guess')
            guess.draw(win)

            #draw hangman structure.
            drawhangman(win)
            #These methods will read the text file and create the blank lines for the word.
            game.difficulty("Hardwordlist.txt")
            game.blankword()

            #Same text objects for the previous levels.
            text.setText('You are playing a hard level')
            text2.setText('Remember:\n You only have 30 seconds \n and 3 wrong guesses!')
            guesstext.draw(win)

            #The variable for the hard level.
            state = 3

        #This condition will be met if the player is on the hard level and presses the guess button.
        # These methods either draw the correct letter in the window or draw a part of the hangman.
        if state ==3 and guessBtn.clicked(pt):
            letter = guess.getText().lower()
            correct = game.getGuess(letter, entryletter)
            if correct == False:
                game.hangmanparts()
                game.drawhangman(state)

        #Game restarts if the new game button is clicked.
        elif newBtn.clicked(pt):
            win.close()
            main()
                       
         #Gets mouse click
        pt = win.getMouse()

    #If the click button is clicked the function closes. Otherwise the next click will restart the game.
    if quitBtn.clicked(pt):
        win.close()
    else:
        win.close()
        main()
        

main()

