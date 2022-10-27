'''
An interpreter for the Bare Bones language. 
The interpreter takes a single argument, the name of a file containing a Bare Bones program. 
It reads the program and executes it.
'''
outputlist=[]
var_dict = {}

def open_file():
    global lineslist
    with open("Challenge3\code.txt","r") as file:
        code = file.read()
        lineslist = code.split(";")
open_file()

def clear(line):
    '''Clears the variable in the line and initializes it to 0'''
    tokens = line.split(" ")
    variable = tokens[1] #the index of the variable in the line is -1
    var_dict[variable] = 0 #sets the variable to 0

def incr(Line):
    '''Increments the variable in the line by 1'''
    tokens = Line.split(" ") #Splits the line into tokens
    var_dict[tokens[1]] += 1 #adds 1 to the variable

def decr(Line):
    '''Decrements the variable in the line by 1'''
    tokens = Line.split(" ")
    var_dict[tokens[1]] -= 1

def end(Line):
    '''Exits the loop or conditional'''
    return

def greater_inequality(Line):
    '''Checks if left variable is greater than right variable'''
    tokens = Line.split(" ")
    true = (var_dict[tokens[1]] > var_dict[tokens[2]])
    if not(true):
        if "else" in Line:
            else_(Line)
        else:
            pass

def lesser_inequality(Line):
    '''Checks if left variable is lesser than right variable'''
    tokens = Line.split(" ")
    true = (var_dict[tokens[1]] < var_dict[tokens[2]])
    if not(true):
        if "else" in Line:
            else_(Line)
        else:
            pass

def add(Line):
    '''Adds both variables in the line'''
    tokens = Line.split(" ")
    var_dict[tokens[1]] += var_dict[tokens[2]]

def sub(Line):
    '''Subtracts both variables in the line'''
    tokens = Line.split(" ")
    var_dict[tokens[1]] -= var_dict[tokens[2]]

def greater_than_inequality(Line):
    '''Checks if left variable is greater than or equal to right variable'''
    tokens = Line.split(" ")
    true = (var_dict[tokens[1]] >= var_dict[tokens[2]])
    if not(true):
        if "else" in Line:
            else_(Line)
        else:
            pass

def lesser_than_inequality(Line):
    '''Checks if left variable is lesser than or equal to right variable'''
    tokens = Line.split(" ")
    true = (var_dict[tokens[1]] <= var_dict[tokens[2]])
    if not(true):
        if "else" in Line:
            else_(Line)
        else:
            pass

def if_(Line):
    '''Executes the code in the if-condition-do loop'''
    tokens = Line.split(" ")
    condition = tokens[2]
    if condition == ">":
        greater_inequality(Line)
    elif condition == "<":
        lesser_inequality(Line)
    elif condition == "==":
        equals(Line)
    elif condition == "!=":
        not_equals(Line)
    elif condition == ">=":
        greater_than_inequality(Line)
    elif condition == "<=":
        lesser_than_inequality(Line)

def not_equals(Line):
    '''Checks if left variable is not equal to right variable'''
    tokens = Line.split(" ")
    true = (var_dict[tokens[1]] != var_dict[tokens[2]])
    if not(true):
        if "else" in Line:
            else_(Line)
        else:
            pass

def equals(Line):
    '''Checks if left variable is equal to right variable'''
    tokens = Line.split(" ")
    true = (var_dict[tokens[1]] ==var_dict[tokens[2]])
    if not(true):
        if "else" in Line:
            else_(Line)
        else:
            pass

def else_(Line):
    '''Executes the code in the else statement'''
    pass

def comments(Line):
    '''Removes comments from the code'''
    pass

def While(Line):
    '''Loops the code in the while-condition-do loop'''
    tokens = Line.split(" ")
    object_to_loop = tokens[1]
    value_of_object = var_dict[object_to_loop]
    while value_of_object!=0:
        if "clear" in Line:
            clear(Line)
        if "incr" in Line:
            incr(Line)
        if "decr" in Line:
            decr(Line)
        if "end" in Line:
            end(Line)
        if "while" in Line: #Nested while loops
            While(Line)

for line in lineslist:
    if "clear" in line:
        clear(line)
    elif "incr" in line:
        incr(line)
    elif "decr" in line:
        decr(line)
    elif "end" in line:
        end(line)
    elif "while" in line:
        While(line)
    elif "if" in line:
        if_(line)
    elif "else" in line:
        else_(line)
    elif "+" in line:
        add(line)
    elif "-" in line:
        sub(line)
    elif "#" in line:
        comments(line)