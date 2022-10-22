'''
An interpreter for the Bare Bones language. 
The interpreter takes a single argument, the name of a file containing a Bare Bones program. 
It reads the program and executes it.
'''
outputlist=[]
var_dict = {}

def open_file():
    global lineslist
    with open("Challenge2\code.txt","r") as file:
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
    '''Ends the Program'''
    tokens = Line.split(" ")
    return

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