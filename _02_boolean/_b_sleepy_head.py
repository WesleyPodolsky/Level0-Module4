"""
Use boolean variables to control program logic between two different code
paths.
"""

from tkinter import messagebox, simpledialog, Tk
import turtle
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO)
    #  1. Use a boolean variable to indicate if it is the weekend.
    #     Display a different message to the user depending on whether it is
    #     the weekend or not.
    isWeekend = False
    if isWeekend:
        messagebox.showinfo(title='sigma', message='its the weekend daddy')
    else:
        messagebox.showinfo(title='erm', message='its NOT the weekend daddy')


    #  2. Use a boolean variable to indicate if a student passed an exam.
    #     Display a different message to the user depending on whether they
    #     passed or not.
    passedExam = False
    if passedExam:
        messagebox.showinfo(title='sigma', message='passed exam')
    else:
        messagebox.showinfo(title='erm', message='no pass examu dumb')
    #  3. Use a boolean variable to indicate if a game is over. When the game
    #     is over, tell the user.
    gameOver = False
    if gameOver:
        messagebox.showinfo(title='sigma', message='game over')

    #  4. Use two boolean variables, one to indicate if a shape should be red,
    #     the other to indicate if the shape is to be square. When both
    #     variables are true, use a turtle to draw a red square.
    shouldRed = True
    shouldSquare = True
    if shouldRed and shouldSquare:
        print('skibiti')
        turtle.mainloop()
        turtle.fillcolor('red')
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(20)
            turtle.left(90)
        turtle.end_fill()
        turtle.done()


