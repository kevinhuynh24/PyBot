import curses
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)


screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

done = False

try:
        while done == False:   
            char = screen.getch()
            if char == ord('q'):
                done = True
            #Rotate both wheels forwards
            elif char == curses.KEY_UP:
                print("up")
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(8,False)
                GPIO.output(10,True)
            #Rotate both wheels backwards
            elif char == curses.KEY_DOWN:
                print("down")
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(8,True)
                GPIO.output(10,False)
            #Rotate left wheel forwards & Rotate right wheel backwards
            elif char == curses.KEY_RIGHT:
                print("right")
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(8,False)
                GPIO.output(10,True)
            #Rotate left wheel backwards & Rotate right wheel forwards
            elif char == curses.KEY_LEFT:
                print("left")
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(8,True)
                GPIO.output(10,False)
            #stop rotation
            elif char == 10:
                print("end")
                GPIO.output(7,False)
                GPIO.output(11,False)
                GPIO.output(8,False)
                GPIO.output(10,False)
             
finally:
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    

