"""
Write a program to return the correct letter grade
"""
from tkinter import messagebox, simpledialog, Tk


# The teacher wants you to write a program that converts the score on 2
# 100 point tests to a letter grade. The teacher wants you to average the
# score from the 2 tests and print out the letter grade back to the user.
# The letter grades are assigned as follows:
#   A = 89.5 to 100
#   B = 79.5 to less than 89.5
#   C = 69.5 to less than 79.5
#   D = 59.5 to less than 69.5
#   F = less than 59.5
if __name__ == '__main__':
    c

    # TODO) Ask the user for their score on the FIRST test and store their
    #  score in a variable
    scoreOne = int(simpledialog.askstring(title='1/2', prompt="What u finna get on you test cuz"))
    # TODO) Ask the user for their score on the SECOND test and store their
    #  score in a variable
    scoreTwo = int(simpledialog.askstring(title='2/2', prompt="whaddu GYAt on ur sencont test rizzer?"))
    # TODO) Take the average score of both tests (total score / 2)
    avgScore = (scoreTwo + scoreOne)/2
    # TODO) Use if statements to check the average score and print the
    #  corresponding letter grade back to the user. Also, give a different
    #  message according to their grade. Example, for an 'A' grade:
    #  "Wow! You must have studied really hard for those tests!"
    if avgScore >= 89.5 and avgScore <= 100:
        messagebox.showwarning(None, 'W mans got bro an A stop sweating')
    elif avgScore >= 75.5 and avgScore <= 89.5:
        messagebox.showwarning(None, 'B is the bes tscore w mans')
    elif avgScore >= 69.5 and avgScore <= 75.5:
        messagebox.showwarning(None, 'C... some people have bad days ig..')
    elif avgScore >= 59.5 and avgScore <= 69.5:
        messagebox.showwarning(None, 'a D!? broski ur cooked')
    elif avgScore <= 59.5:
        messagebox.showwarning(None, 'imaging getting an F like cuz how')
    pass
