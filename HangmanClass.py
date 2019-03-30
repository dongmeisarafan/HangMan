#Guin Feldman and Dong Mei Sarafan
#Final Project: Hangman Class
#Due Date: May 18, 2016

import random
from graphics import *
from audioplayer import *
from time import *
class Hangman():

    def __init__(self, win):
        """ This constructor intializes values to be used later in the program.
    The graphics window, word, lists for the player's guesses, and the boolean statement to determine
    if the game is over are all intialized in this constructor. It takes the graphics window as a parameter."""
        #Initializing lists and variables to use throughout the program
        self.win = win
        self.word = ""
        self.guesses = []
        self.missguess = []
        self.correctletters = []
        self.miss = 0
        self.end = False

    def difficulty(self, wordfile):
        """This method opens and reads a word document.
It then splits up the file into individual words and selects a random word from the list.
It takes a wordfile as a parameter."""
        #This opens and reads a wordfile.
        self.wordfile = open(wordfile, "r", encoding='utf-8').read()
        #This splits the file into individual words.
        words = self.wordfile.split()
        #This selects a random word.
        self.word = random.choice(words)
       

    def getGuess(self, letter, entryletter):
        """ This method takes in a guess and compares the guess to letters in the word.
If the letter is in the word, the letter is displayed in the graphics window. Otherwise, a part
of the hangman is drawn. The method returns a boolean statement to determine whether a guess was correct or not.
The parameters for the method are letter and entryletter.The entryletter parameter is used to display
every guess that the player guesses."""
        #This is an accumulator that will be used to print each letter on the line that it corresponds to
        i = 0
        #This boolean statement is used to check if the letter is in the word.
        correct = False
        #This for loop goes through each character in the word.
        for ch in self.word:
            #This statement checks if the letter is equal to a character in the word.
            if letter == ch:
                #If the letter is in the word, the boolean statement becomes true.
                correct = True
                #This statement finds the X-value for the middle of each blank line.
                letterpointX = self.linelist[i].getcenterX()
                #This draws each letter in the middle of each blank line that it corresponds to.
                self.drawletter = Text(Point(letterpointX, 6), letter)
                self.drawletter.setSize(20)
                self.drawletter.draw(self.win)
                #This appends the drawn letters to a list of correct letters guessed.
                self.correctletters.append(self.drawletter)
                #This statement is a sound effect played when the person guesses a correct letter in the word.
                startSound('Yessound.mp3', async=True, loop=False)
            #Shift the accumulator over 1 spot
            i = i +1

        #If the letter is incorrect
        if correct == False:
            #If the letter is incorrect and is not already in a list of wrong guesses, it is appended to the list self.missguess
            if letter not in self.missguess:
                self.missguess.append(letter)
            else:
                #This makes sure that if a wrong letter is guessed twice only one part of the hangman will be drawn.
                self.miss = self.miss - 1
        #This appends each guess to a list of guesses - only appends it once.
        if letter not in self.guesses:
            self.guesses.append(letter)

        #This is an accumulator.
        guess = ""
        #This goes through each guess in the list of guesses
        for ch in self.guesses:
            #This draws each guessed letter in the graphics window.
            guess = guess + " "+ ch
        entryletter.setText(guess)
        entryletter.setSize(15)
        #This returns the value of the boolean statement correct to the main function, which says whether or not the letter guessed was correct or not.
        return correct

    def hangmanparts(self):
        """This method creates the different parts of the hangman and appends the parts to a list
to be used for later reference."""
        #List of the hangman parts
        self.hangman =[]
        #This creates each part of the hangman.
        head = Circle(Point(9,16.5),0.5)
        self.hangman.append(head)
        body = Line(Point(9,16), Point(9,14))
        self.hangman.append(body)
        arm1 = Line(Point(9,15.5), Point(8.5,16))
        self.hangman.append(arm1)
        arm2 = Line(Point(9,15.5), Point(9.5,16))
        self.hangman.append(arm2)
        leg1 = Line(Point(9,14), Point(8.5,13.5))
        self.hangman.append(leg1)
        leg2 = Line(Point(9,14), Point(9.5,13.5))
        self.hangman.append(leg2)
        eye1 = Point(8.75, 16.5)
        self.hangman.append(eye1)
        eye2 = Point(9.25,16.5)
        self.hangman.append(eye2)
        mouth = Line(Point(8.75, 16.25), Point(9.25,16.25))
        self.hangman.append(mouth)

    def drawhangman(self, level):
        """This method draws a part of the hangman for each wrong guess. The amount of parts
drawn at once depend on the level of the game. The parameter for this method is the level."""
        #accumulator for the number of body parts that have been drawn.
        bodypart = 9
        #If we are on the easy level and parts of the hangman have been drawn this will run.
        if level > 0 and bodypart > 0:
            #If the number of wrong guesses is equal to then number of parts of the hangman, then the player loses the game.
            if not ((self.miss) >= len(self.hangman)):
                #This draws each part of the hangman everytime the player guesses a wrong letter.
                self.hangman[self.miss].draw(self.win)
                #This changes the value of the accumulator bodyparts - tells how many body parts have been drawn already.
                bodypart -= 1
                #Sound effect if the player guesses a wrong answer.
                startSound('Nosound.mp3', async=True, loop=False)
                
        #This is for the medium level and if more than 1 body part is left
        if level > 1 and bodypart > 1:
            #If the number of missed guesses is greater than the length of the body parts of the hangman.
            #Same statements to the previous if statement
            if not (self.miss + 1 >= len(self.hangman)):
                #This draws a part of the hangman and accumulates the number of body parts drawn.
                self.hangman[self.miss + 1].draw(self.win)
                bodypart -= 1
            #For the medium level, the program will first go through the first if statement, and then this one, allowing the program to draw two parts of the hangman at once.

        #This if statement will work for the hard level. 
        if level > 2 and bodypart > 2:
            #Same as the previous if statements. 
            if not (self.miss + 2 >=  len(self.hangman)):
                #This draws a part of the hangman and accumulates the number of body parts drawn.
                self.hangman[self.miss + 2].draw(self.win)
                bodypart -= 1
        #This adds 1 to the number of wrong guesses.
        self.miss = self.miss + level
        


    #This method creates blank lines to display the words.
    def blankword(self):
        """This method is used to give the player a hint at the word by drawing the number
of blank lines that correspond to the length of the word."""
        #This is an empty list for the lines created.
        self.linelist = []
        #The number of lines is equal to the length of the word.
        numofLines = len(self.word)
        #The x-coordinate for the first line.
        pt1X = 2
        distance = 16
        center = distance//numofLines
        #This for loop creates a line for each letter in the word.
        for i in range(numofLines):
            #These statements change the distance between each line depending on how many letters are in the word.
            pt1X = center * (i) + center
            newline = Line(Point(pt1X,5), Point(pt1X + 1, 5))
            newline.draw(self.win)
            #The new line is appended to the list of lines.
            self.linelist.append(newline)

    #This method is used for the timer.
    def clock(self):
        """This method tells the player when time is up and the game is over.
It returns a boolean statement to tell the program that the game is over."""
        #It tells the user that time is up and returns a boolean value.
        timer = Text(Point(15,13), "Times Up!")
        timer.setSize(25)
        timer.setFill('red')
        timer.draw(self.win)
        self.end = True

    #This method is used when the player wins the game.
    def wingame(self):
        """This method is used to tell the player that they won the game if the word is
determined within the time and guess limit. It returns a boolean statement to tell the program
that the game is over."""
        #If the number of correct guesses equals the length of the word, then this condition will run.
        if len(self.correctletters) == len(self.word) and len(self.correctletters) > 0:
            #This statement tells the user to either click and restart the game or quit out of the game.
            nextstep = Text(Point(10,4), "Click to play a new game or click the quit button to stop playing!")
            nextstep.setSize(15)
            nextstep.setFill('blue')
            nextstep.draw(self.win)

            #This statement tells the player that they won.
            won = Text(Point(10,8), "You Won!")
            won.setSize(20)
            won.setFill("green")
            won.draw(self.win)

            #Returns a boolean value to tell the program to end the game.
            return True

    #This method is if the player loses the game.
    def losegame(self):
        """This method is used to tell the player that they lost the game and will give them the correct answer.
The player loses if they did not guess the word in time or have reached the amount of wrong guesses
they can have for each letter."""
        #This statement runs if the number of wrong guesses is greater than or equal to 9 (which is the number of parts of the hangman) or if the time runs out.
        if self.miss >= 9 or self.end:
            #This tells the player that they have lost the game. 
            losttext = Text(Point(10,8), "You Lost! Game Over!")
            losttext.setSize(20)
            losttext.setFill("red")
            losttext.draw(self.win)
            #This tells the player to either click to restart the game or click the quit button to stop playing.
            nextstep = Text(Point(10,4), "Click to play a new game or click the quit button to stop playing!")
            nextstep.setSize(15)
            nextstep.setFill('blue')
            nextstep.draw(self.win)

            #accumulator
            i = 0
            #This for loop is used to display the entire word if the player loses.
            for ch in self.word:
                letterpointX = self.linelist[i].getcenterX()
                self.drawletter = Text(Point(letterpointX, 6), ch)
                self.drawletter.setSize(20)
                self.drawletter.draw(self.win)
                i = i + 1
            #returns boolean statements to determine whether the game is over or not.
            return True
        else:
            return False
            #deactivate the entry box - could do that in main
            

        
