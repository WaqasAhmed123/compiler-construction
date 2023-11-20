import string
import re
import tabulate
dataTypes = ["int", "str", "float", "bool", "char"]
keywords=["if","else","else if","main","for","break","continue","while", "Public", "Main", "var"]
punctuators = ['{', '}', '(', ')', '[', ']', ';']
singleComment = "#"
multiLineComment = '$$$'
# ---------------------------------------------
arithmetic = ['+', '-', '*', '/', '//', '%']
assignment = ['+=', '-=', '*=', '/=', '%=','=']
comparison = ['==', '!=', '<', '>', '<=', '>=']
logical = ['&&', '||', '!']
bitwise = ['&', '|', '^', '~', '<<', '>>']
increment = ['++', '--']
ternary = ['?']
operators = arithmetic + assignment + comparison + logical + bitwise + increment + ternary
stringCheckFlag=False


words = []
def customWordSplitter(lines):
    skip_iterations = 0
    global multiLineComment
    multiLineCommentFlag=False
    global words
    lexeme = ""
    findingString=False 
    doubleOperator=False
    for line in lines:
        for index in range(len(line)):
            char = line[index]
            
            if skip_iterations > 0:
                skip_iterations -= 1
                continue
            if char == "$":
                if(line[index+2] and char+line[index+1]+line[index+2])==multiLineComment:
                    
                    print("char checked ",char+line[index+1]+line[index+2])
                    multiLineCommentFlag= not multiLineCommentFlag
                    skip_iterations = 2
                    continue
                    
            if multiLineCommentFlag:
                print("checked line",line)
                continue
            if char == singleComment:
                break
            # elif(char=='"'):
            #     if (lexeme):
            #         if findingString==True:
            #             lexeme+='"'
            #             words.append(lexeme)
            #             lexeme=""
            #             # continue
            #         else:
            #             words.append(lexeme)
            #             lexeme='"'
            #     else:
            #         lexeme='"'
            #     findingString=not findingString
            # elif findingString:
            #     lexeme+=line[index]
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
                    break
                    
                
                if lexeme:
                    words.append(lexeme)
                    lexeme = ""
                if line[index+1]:
                    # print("in second if",char)
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
        # print("last",lexeme)

        if lexeme:
            print("at last",lexeme)
            words.append(lexeme)
            lexeme = ""

    return words

f = open("file_to_split.txt", "r",encoding="utf-8")
data = f.read()
data=data.split("\n")
linesList=[]
for line in data:
    linesList.append(line+'\n')


result = customWordSplitter(linesList)
print(linesList)
print(words)




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


# Create instances of the Token class based on the words
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
        t.CP="float"
    elif (word in operators):
        
        t.CP=findOperatorType(word)
    else:
        t.CP="undefined"
    Tokens.append(t)
# for token in Tokens:
#     print(token.CP, token.VP, token.LN)
# print()
table_data = [(token.CP, token.VP, token.LN) for token in Tokens]

# Print the table
print(tabulate.tabulate(table_data, headers=["CP", "VP", "LN"], tablefmt="fancy_grid"))