'''
Lori Hunt
Program Lesson 1_3_2   AP CSP's first stab at writing functions
Run this and 
'''
import math  # I have to do this to use the sqrt function on line 12


def quadFormula(a=1, b=1, c=-1):
    '''This function will find the solutions to a quadratic
     '''
    discriminant = b ** 2 - 4 * a * c
    numerator1 = -b + math.sqrt(discriminant)
    # numerator2 = <you fill this in!!>
    denominator = 2 * a
    x1 = numerator1 / denominator
    # x2 = <you fill this in>
    return x1  # you will include x2 once you find it


def beNice():
    '''supply your name and receive a positive affirmation!'''
    name = input("Enter your name ")
    message = name + ", you are so smart! "
    return message + " You are beautiful " + name


def circle():
    radius = int(input("Enter the radius "))
    return radius ** 2 * 3.14


'''
Do this with your partner:
    A.  Run the beNice and circle functions first!!
    run them from the console and from the program.
    1. Describe how you do each here:
        console-
       
        
          
        program - 
    

    2.  Change circle() so that it takes in a parameter representing the radius
    instead of asking the user for the radius. Put comments under the definition
    of circle with block comments (three single quotes)
    
    a) What does your function name look like now?
    
    
    
    b) Call on the circle function from the console and from the program.
    Describe how you do that here:
       
        console -
       
        
          
        program -
    
    
    3.  Run the quadFormula function.  Once you understand how it is 
    working, complete this function by filling in the missing code.
    Write what you filled in here
    
    #numerator2 = <you fill this in!!>
    
    #x2 = <you fill this in>
    
    return x1  #you will include x2 once you find it
    
    
      a)  What do you notice is different about the parameters in
         this function?  What happens if you put in 1, -8 and 15
         for a, b, and c
    
      b)  Don't send any parameters to quadFormula, what output are you given?
    
    
    4.  Write code in this program (but not in a function!) that asks the user 
    to enter the length and width of a rectangle. Test it and make sure
    it works (Write these on the back)
    
    a) Write a function that finds and returns the perimeter of any 
    rectangle. Your header should be:
        def perimater(len = 1, wid = 1):
    
    ** Test this function!
    b) Write a function that finds and returns the area of a rectangle
        def area(len = 1, wid = 1):
            
    ** Test this function!!
    c) Write a function that will draw the rectangle
        def draw(len = 1, wid = 1):
            
    **Test this function!!
            
    
    
'''
