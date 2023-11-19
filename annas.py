
import re
S = ['Public int Main()\n', '{\n', '  int a = 7;\n', '  a++\n', '  while(a<S)\n', '   {\n', '     var str = "Hello World";\n', '     a--\n', '   }\n', '}']
    
punctuators = ['{', '}', '(', ')', '[', ']', ';',"'"]
single_comment = "#"
multi_comment = ' """'
new_line="/n"
arithmetic = ['+', '-', '*', '/', '//', '%']
assignment = ['=','+=', '-=', '*=', '/=', '%=']
comparison = ['==', '!=', '<', '>', '<=', '>=']
logical = ['&&', '||', '!']
bitwise = ['&', '|', '^', '~', '<<', '>>']
increment = ['++', '--']
ternary = ['?']
dataTypes=["int","str","float","bool","char",]
keywords=["if","else","else if","main","for","break","continue","while", "Public", "Main", "var"]
separators = punctuators
operators = arithmetic + assignment + comparison + logical + bitwise + increment + ternary
# sadasdas;
lexeme = ""
words = []

def isSpace(char):
    if char==" ":
        return True
    else:
        return False

def isSeperator(char):
    if char in separators:
        return True
    else:
        return False

def isOperator(char):
    if char in operators:
        return True
    else:
        return False
def isStringWord(char,line,index):
    string=""
    if (char=='"'):
        return True
    else:
        return False
        # i=index+1
        # while True:
        #     if (line[i]):
        #         string+=line[i]
        #         if line[i]=
                
                
        

def isNewLine(char):
    if char == new_line:
        return True
    else:
        return False

def isComment(char):
    if char == single_comment:
        return True
    else:
        return False

def isMultilineComment(line,index,multiLineComment):
    if (line[index]=='"'):
            if (line[index+1] and line[index+2]):
                if (line[index+1] =='"' and line[index+2]=='"'):
                    return not multiLineComment

# def isLexeme():
#     if(lexeme):
#         return True
#     else:
#         return False

multiLineComment=False 
complexOperator=False
findingString=False   

for line in S:
    for index in range(len(line) - 1):
        # print(line)
        if line[index] == "\n":
            print("found")
        if(isMultilineComment(line,index,multiLineComment)):
            multiLineComment=not multiLineComment
            break
        # if (multiLineComment):
        #     print("mlc")
        #     break
        
        elif(isStringWord(line[index],line,index)):
            if (lexeme):
                if findingString==True:
                    lexeme+='"'
                    words.append(lexeme)
                    lexeme=""
                    # continue
                else:
                    words.append(lexeme)
                    lexeme='"'
            else:
                lexeme='"'
            findingString=not findingString
            
                
            # lexeme+='"'
            # continue   
        elif findingString:
           lexeme+=line[index]
        elif (isComment(line[index])):
            break
        elif (isSpace(line[index]) ):
            if (lexeme):
                words.append(lexeme)
                lexeme=""
        elif (isOperator(line[index])):
            if (lexeme):
                words.append(lexeme)
                lexeme=""
            if isOperator(line[index+1]):
                lexeme+=line[index]+line[index+1]
                complexOperator=True
            else:
                if(not complexOperator):
                    words.append(line[index])    
        elif (isSeperator(line[index])):
            if (lexeme):
                words.append(lexeme)
                lexeme=""
            words.append(line[index])
        elif (isNewLine(line[index])):
            if (lexeme):
                words.append(lexeme)
                lexeme=""
            words.append(line[index])
        else:
            lexeme+=line[index]
    words.append('\n')
           


# tokenizer
tokenizer=[]
token={}
variables=[]

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
def isVariable(word):
    if word in variables:
        return True
    else:
        return False
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
    token= {
                "word":word,
                "type":"",
                "line_number":lineNumber
            }
    if (isKeyword(word)):
        token["type"]="keyword"
    elif (isDatatype(word)):
        token["type"]="datatype"
    elif (isOperator(word)):
        token["type"]=findOperatorType(word)
    elif (isSeperator(word)):
        token["type"]=word
    elif (isString(word)):
        token["type"]="string"
    elif (isChar(word)):
        token["type"]="char"
    elif (isInt(word)):
        token["type"]="integer"
    elif (isFloat(word)):
        token["type"]="float"
    else:
        token["type"]="undefined"
            
    tokenizer.append(token)
    token={}        

print()
print()
print()
print("==================THE CODE IS==================")
print()
print(S)
print()
print("==================WORD SPLITTER==================")
print()
print(words)
print()
print("==================TOKENIZER==================")
print()
print(words)
for value in tokenizer:
    if value["type"]:
        print(value["word"], end="\t\t")
        print(value["type"], end="\t\t\t")
        print(value["line_number"])