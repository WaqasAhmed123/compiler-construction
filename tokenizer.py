# import string
import re
import tabulate
dataTypes = ["int", "str", "double", "bool", "char"]
keywords=["if","else","elif","main","for","break","continue","while", "Public", "Main", "var"]
punctuators = ['{', '}', '(', ')', '[', ']', ';']
singleComment = "#"
multiLineComment = '$$$'
# ---------------------------------------------
arithmetic = ['+', '-', '*', '/', '//', '%']
assignment = ['+=', '-=', '*=', '/=', '%=','=']
comparison = ['==', '!=', '<', '>', '<=', '>=']
logical = ['&&', '||', '!']
bitwise = ['&', '|', '^', '~', '<<', '>>']
increment = ['++']
decrement = ['--']
ternary = ['?']
operators = arithmetic + assignment + comparison + logical + bitwise + increment + decrement+ ternary

# word splitter takes linesList as a parameter and return splitted words-----------------------
words = []
def customWordSplitter(lines):
    stringCheckFlag=False
    skipIterations = 0
    global multiLineComment
    multiLineCommentFlag=False
    global words
    lexeme = ""
    doubleOperator=False
    for line in lines:
        for index in range(len(line)):
            char = line[index]
            
            if skipIterations > 0:
                skipIterations -= 1
                continue
            elif char == "$":
                if(line[index+2] and char+line[index+1]+line[index+2])==multiLineComment:
                    multiLineCommentFlag= not multiLineCommentFlag
                # if not multiLineCommentFlag and skipIterations==1 and line[index+2] and line[index+1]+ line[index+2]=='\n': 
                # if not multiLineCommentFlag : 
                #     print("found",line[index+2])
                    
                #     skipIterations = 4
                # else:
                    skipIterations = 2
                    # print("second if")
                    continue
                    
                
                    
            elif multiLineCommentFlag:
                continue
            elif char == singleComment:
                break
            elif(char=='"'):
                stringCheckFlag=not stringCheckFlag
                lexeme+=char
                if  stringCheckFlag==False:
                    words.append(lexeme)
                    lexeme=""
                    continue
                else:
                    continue
            elif stringCheckFlag:
                lexeme+=char
                continue
            elif char == '\n':
                if lexeme:
                    words.append(lexeme)
                    lexeme = ""
                words.append('\n')    
            elif char == " ":
                if lexeme:
                    words.append(lexeme)
                    lexeme = ""
            elif char in operators:
                if doubleOperator:
                    doubleOperator=False
                    lexeme=""
                    continue
                    
                if lexeme:
                    words.append(lexeme)
                    lexeme = ""
                if line[index+1]:
                    if line[index+1]+char in operators:
                        lexeme+=char+line[index+1]
                        words.append(lexeme)
                        lexeme=""
                        doubleOperator=True
                    else:
                        lexeme+=char
                        words.append(lexeme)
                        lexeme=""
                else:
                    print("caught",char)
                    lexeme+=char
                    words.append(lexeme)               
                    lexeme=""
            elif char in punctuators:
                if lexeme:
                    words.append(lexeme)
                    lexeme = ""
                words.append(char)
            else:
                lexeme += char

        if lexeme:
            words.append(lexeme)
            lexeme = ""

    return words

#read the txt file and create linesList accordingly --------------------------
f = open("file_to_split.txt", "r",encoding="utf-8")
data = f.read()
data=data.split("\n")
linesList=[]
for line in data:
    linesList.append(line+'\n')


result= customWordSplitter(linesList)
# print(linesList)



# functions for CP mostly-------------------------------------
def isKeyword(word):
    if word in keywords:
        return True
    else:
        return False
def isDatatype(word):
    if word in dataTypes:
        return True
    else:
        return False
def findOperatorType(word):
    if word in assignment:
        return "assignment" 
    elif word in arithmetic:
        return "arithmetic" 
    elif word in comparison:
        return "comparison" 
    elif word in logical:
        return "logical" 
    elif word in bitwise:
        return "bitwise" 
    elif word in increment:
        return "increment" 
    elif word in decrement:
        return "decrement" 
    elif word in ternary:
        return "ternary" 

def isString(s):
    return re.match(r'^".*"$', s) is not None

def isChar(s):
    return re.match(r'^[a-zA-Z]$', s) is not None

def isFloat(s):
    return re.match(r'^[+-]?\d*\.\d+$', s) is not None

def isInt(s):
    return re.match(r'^[+-]?\d+$', s) is not None

# Tokenization part-------------------------------
Tokens = []
class Token:
    def _init_(self):
        self.CP = None
        self.VP = None
        self.LN = None


lineNumber=1
for word in words:
    if word=='\n':
        lineNumber += 1
        continue
    t = Token()
    t.VP=word
    t.LN=lineNumber
    if (isKeyword(word)):
        t.CP="keyword"
    elif (isDatatype(word)):
        t.CP="datatype"
    elif (word in punctuators):
        t.CP=word
    elif (isString(word)):
        t.CP="string"
    elif (isChar(word)):
        t.CP="char"
    elif (isInt(word)):
        t.CP="integer"
    elif (isFloat(word)):
        t.CP="double"
    elif (word in operators):
        
        t.CP=findOperatorType(word)
    else:
        t.CP="undefined"
    Tokens.append(t)
# for token in Tokens:
#     print(token.CP, token.VP, token.LN)
# print()
tableData = [(token.CP, token.VP, token.LN) for token in Tokens]

# Print the table
print(tabulate.tabulate(tableData, headers=["CP", "VP", "LN"], tablefmt="fancy_grid"))
# print(words)


