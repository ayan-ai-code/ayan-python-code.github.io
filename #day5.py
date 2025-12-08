#day5

print (" hello my name is ayan \n and i am \"20\" year old")
# \n is used for new line is called escape sequence
#[\"]backslash is used to escape the character and it is called escape sequence  and it is used to print double quote inside double quote
print ('hello' , 9 , True , sep="-" , end='007\n')
print ("ayan")
#other parameter of print statement
#object(s)
#sep='seperator'
#end='end'
#file : an object with a write method . default os sys.stdout

a='stringing'
b= 2
print (a + str(b))
#i cant add string and integer so i have to convert integer into string using "str" function

c="\033[1m dance\033[1m"
d= "\n\"  1  \" \n\"  2  \"\n\"  3  \""
e = "\n\033[3m  GO\033[1m"
print (c + d + e)
#"\033[1m word \033[1m": is used to make word bold 

x = "counting"
y = x[2]
print(y)
#to print first letter of string we have to use [0] #and to print last letter we have to use [-1] 
#and to print whole string we have to use [0:-1]

'''
IMPORTANT TYPE OF BRACKETS IN PYTHON:

'''
# Square Brackets [ ]:
# Used for indexing and slicing strings/lists
# Example from your code: x[0] gets the first character of string x
# Parentheses ( ):
# Used for function calls and grouping expressions
# Example from your code: print("hello world")
# Curly Braces { }:
# Used for creating dictionaries
# Used for creating sets
# Not shown in your current code, but example: my_dict = {"key": "value"}
# Triple Quotes """ """ or ''' ''':
# Used for multiline strings/comments
# Example from your code:
