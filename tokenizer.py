# import string
import re
import tabulate
dataTypes = ["int", "string", "double", "bool", "char"]
keywords=["if","else","elif","main","for","break","continue","while", "Public", "Main", "var","interface",'return']
punctuators = ['{', '}', '(', ')', '[', ']', ';','.']
singleComment = "#"
multiLineComment = '$$$'
# ---------------------------------------------
arithmetic = ['+', '-', '*', '/', '//', '%']
assignment = ['+=', '-=', '*=', '/=', '%=','=']
comparison = ['<=', '>=','==', '!=', '<', '>', ]
logical = ['&&', '||', '!']
bitwise = ['&', '|', '^', '~', '<<', '>>']
increment = ['++']
decrement = ['--']
ternary = ['?',':']
operators = arithmetic + assignment + comparison + logical + bitwise + increment + decrement+ ternary


def isInt(s):
    return re.match(r'^[+-]?\d+$', s) is not None
# word splitter takes linesList as a parameter and return splitted words-----------------------
words = []
def customWordSplitter(lines):
    iterationsToSkip=0
    stringCheckFlag=False
    doubleCheckFlag=False
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
                    skipIterations = 2
                    continue
            elif multiLineCommentFlag:
                continue
            elif char == singleComment:
                break
            elif(char=='"' or char =="'"):
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
            # elif index + 1 < len(line) and char + line[index + 1] == '\n':
            # elif line[index+1] and  char+line[index+1] == '\n':
            elif char == '\n':
            # elif char == '\\' and line[index+1] and line[index+1]=="n":
                if lexeme:
                    words.append(lexeme)
                    lexeme = ""
                words.append('\n')
                # skipIterations=1    
            elif char == " ":
                if lexeme:
                    words.append(lexeme)
                    lexeme = ""
            elif char in operators:

                if lexeme:
                    words.append(lexeme)
                    lexeme = ""
                if line[index+1]:
                    if char+line[index+1] in operators:
                        lexeme+=char+line[index+1]
                        words.append(lexeme)
                        lexeme=""
                        skipIterations = 1
                            
                    else:
                        lexeme+=char
                        words.append(lexeme)
                        lexeme=""
                else:
                    lexeme+=char
                    words.append(lexeme)               
                    lexeme=""
                             
                
            elif char in punctuators:
                if lexeme:
                    if char =='.' and isInt(lexeme):
                        lexeme += char
                        if not doubleCheckFlag:
                            # lexeme += char
                            
                            for next_index in range(index + 1, len(line)):
                                if line[next_index].isdigit():
                                    print("char is ",line[next_index])
                                    lexeme += line[next_index]
                                    iterationsToSkip+=1
                                else:
                                    doubleCheckFlag=not doubleCheckFlag
                                    words.append(lexeme)
                                    skipIterations=iterationsToSkip
                                    lexeme=""
                    else:
                        if lexeme:
                            words.append(lexeme)
                            lexeme = ""
                            lexeme += char
                            words.append(lexeme)
                            lexeme = ""
                else:
                    lexeme+=char
                    words.append(lexeme)
                    lexeme=""
            else:
                lexeme += char
                print("got",lexeme)
                if lexeme=="\\n":
                    print("got real",lexeme)
                    words.append('\n')
                    # words.append(lexeme)
                    lexeme=""
                
            
        if lexeme:
                
            print("last if",lexeme)
            words.append(lexeme)
            lexeme = ""

    return words

#read the txt file and create linesList accordingly --------------------------
f = open("file_to_split.txt", "r",encoding="utf-8")
data = f.read()
data=data.split('\n')
linesList=[]
for i, line in enumerate(data):
    if i < len(data) - 1:
        linesList.append(line + '\n')
    else:
        linesList.append(line)
# for line in data:
#     if(line.index < len(data)):
#         linesList.append(line+'\n')
#     else:
#         linesList.append(line)
        
    # linesList.append('\n')


result= customWordSplitter(linesList)
print(linesList)



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
    return re.match(r'^["\'].*["\']$', s) is not None

def isChar(s):
    return re.match(r'^[a-zA-Z]$', s) is not None

def isFloat(s):
    return re.match(r'^[+-]?\d*\.\d+$', s) is not None

def isVariable(s):
    return re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', s) is not None




# Tokenization part-------------------------------
Tokens = []
class Token:
    def _init_(self):
        self.CP = None
        self.VP = None
        self.LN = None


lineNumber=1
for word in words:
    # if word=='\n':
    #     lineNumber += 1
        # continue
    t = Token()
    t.VP=word
    t.LN=lineNumber
    if (isKeyword(word)):
        t.CP="keyword"
    elif word=="\n":
        t.CP="new line"
        lineNumber += 1
        t.VP='\\n'
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
    elif (isVariable(word)):
        t.CP="ID"
    elif (word in operators):
        t.CP=findOperatorType(word)
    else:
        t.CP="undefined"
    Tokens.append(t)
    # if word=='\n':
    #     lineNumber += 1
# for token in Tokens:
#     print(token.CP, token.VP, token.LN)
# print()
tableData = [(token.CP, token.VP, token.LN) for token in Tokens]

# Print the table
print(tabulate.tabulate(tableData, headers=["CP", "VP", "LN"], tablefmt="fancy_grid"))
print(words)  


