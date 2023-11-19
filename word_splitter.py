
import string
import re
dataTypes = ["int", "String", "float", "bool", "char"]
keywords=["if","else","else if","main","for","break","continue","while", "Public", "Main", "var"]
punctuators = ['{', '}', '(', ')', '[', ']', ';']
singleComment = "#"
multiComment = ' """'
arithmetic = ['+', '-', '*', '/', '//', '%']
assignment = ['+=', '-=', '*=', '/=', '%=','=']
comparison = ['==', '!=', '<', '>', '<=', '>=']
logical = ['&&', '||', '!']
bitwise = ['&', '|', '^', '~', '<<', '>>']
increment = ['++', '--']
ternary = '?'
# singleCharElements=['+', '-', '*', '/','=','<','>','!','&', '|', '^', '~','%']
doubleCharElements=['+=', '-=', '*=', '/=', '%=','<=', '>=''&&', '||','++', '--']

stringCheck=False
multiCommentChecked=True

class Token:
    def __init__(self):
        self.CP = None
        self.VP = None
        self.LN = None

words = []

def customWordSplitter(lines):
    global words
    lexeme = ""
    
    for line in lines:
        for index in range(len(line)):
            char = line[index]
            if char == multiComment:
                multiLineComment = not multiLineComment
                break
            elif char == singleComment:
                break
            elif char == " ":
                if lexeme:
                    words.append(lexeme)
                    lexeme = ""
            elif char in arithmetic:
                # print("found",lexeme)
                if lexeme:
                    if(index<len(line) and char+line[index+1] in doubleCharElements):
                        # print("fhakj")
                        words.append(lexeme)
                        lexeme=""
                        lexeme+=char+line[index+1]
                        words.append(lexeme)
                        lexeme=""
                        
                    else:
                        words.append(lexeme)
                        words.append(char)
                        lexeme=""
            elif char in assignment:
                if lexeme:
                    if(index<len(line) and char+line[index+1] in doubleCharElements
                    #    or char + line[index + 1] in increment
                       ):
                        words.append(lexeme)
                        lexeme=""
                        # print("fhakj")
                        lexeme+=char+line[index+1]
                        words.append(lexeme)
                        lexeme=""
                    else:
                        words.append(lexeme)
                        words.append(char)
                        lexeme=""
                
            elif char in assignment:
                if lexeme:
                    words.append(lexeme)
                    lexeme = ""
                words.append(char)
            elif char in punctuators:
                if lexeme:
                    words.append(lexeme)
                    lexeme = ""
                words.append(char)
            else:
                lexeme += char
        # print("last",lexeme)

        if lexeme:
            words.append(lexeme)
            lexeme = ""

    return words
# Read Word document content using open
file_path = "file_to_split.txt"
with open(file_path, 'r', encoding='utf-8') as file:
    text_from_file = file.read()
    for line in text_from_file:
        lineWiseData = text_from_file.split("\n")
        

# Use the custom word splitter
result = customWordSplitter(lineWiseData)

# Create instances of the Token class based on the words
Tokens = []

# annas 
def isKeyword(word):
    # print("key")
    if word in keywords:
        return True
    else:
        return False
def isDatatype(word):
    if word in dataTypes:
        return True
    else:
        return False
# def isVariable(word):
#     if word in variables:
#         return True
#     else:
#         return False
# arithmetic + assignment + comparison + logical + bitwise + increment + ternary
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

lineNumber=1
for word in words:
    if word=='\n':
        lineNumber += 1
        continue
    t = Token()
    
    # if word in punctuators:
    #     t.CP = "ID"
    #     t.VP = word
    #     t.LN = "line"
    # Tokens.append(t)
    
    # token= {
    #             "word":word,
    #             "type":"",
    #             "line_number":lineNumber
    #         }
    t.VP=word
    t.LN=lineNumber
    if (isKeyword(word)):
        t.CP="keyword"
    elif (isDatatype(word)):
        t.CP="datatype"
    # elif (isOperator(word)):
    #     token["type"]=findOperatorType(word)
    # elif (isSeperator(word)):
    #     token["type"]=word
    # elif (isString(word)):
    #     token["type"]="string"
    elif (isChar(word)):
        t.CP="char"
    elif (isInt(word)):
        t.CP="integer"
    elif (isFloat(word)):
        t.CP="float"
    else:
        t.CP="undefined"
            
    Tokens.append(t)

# annas
# for word in words:
#     t = Token()
#     if word in punctuators:
#         t.CP = "ID"
#         t.VP = word
#         t.LN = "line"
#     Tokens.append(t)

for token in Tokens:
    print(token.CP, token.VP, token.LN)

print(lineWiseData)

