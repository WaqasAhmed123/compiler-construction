# from docx import Document
# import string

# punctuators = ['{', '}', '(', ')', '[', ']', ';']
# singleComment = "#"
# multiComment = ' """'
# arithmetic = ['+', '-', '*', '/', '//', '%']
# assignment = ['+=', '-=', '*=', '/=', '%=']
# comparison = ['==', '!=', '<', '>', '<=', '>=']
# logical = ['&&', '||', '!']
# bitwise = ['&', '|', '^', '~', '<<', '>>']
# increment = ['++', '--']
# ternary = '?'

# class Token:
#     def __init__(self):
#         self.CP=None 
#         self.VP =None
#         self.LN =None

# words = []

# def customWordSplitter(text):
#     currentWord = ""

#     for char in text:
#         # If the character is a letter or a digit, add it to the current word
#         if char.isalnum() or char in string.punctuation:
#             currentWord += char
#         else:
#             # If the current word is not empty, add it to the list of words
#             if currentWord:
#                 words.append(currentWord)
#                 currentWord = ""

#     # Add the last word if the text ends with a letter or digit
#     if currentWord:
#         words.append(currentWord)

#     return words

# # Read Word document content using open
# file_path = "file_to_split.txt"
# with open(file_path, 'r', encoding='utf-8') as file:
#     text_from_file = file.read()
# # Use the custom word splitter
# result = customWordSplitter(text_from_file)

# # Create instances of the Token class based on the words
# Tokens = []
# for word in words:
#     t = Token()
#     if(word in punctuators):
#         t.CP="ID"
#         t.VP=word
#         t.LN="line"
#     Tokens.append(t)
# for token in Tokens:
#     print(token.CP,token.VP,token.LN)
# print(words)



punctuators = ['{', '}', '(', ')', '[', ']', ';']
single_comment = "#"
multi_comment = ' """'
arithmetic = ['+', '-', '*', '/', '//', '%']
assignment = ['+=', '-=', '*=', '/=', '%=']
comparison = ['==', '!=', '<', '>', '<=', '>=']
logical = ['&&', '||', '!']
bitwise = ['&', '|', '^', '~', '<<', '>>']
increment = ['++', '--']
ternary = '?'
dataTypes=["int","String","float","bool","char",]
keywords=["if","else","else if","main","for","break","continue","while"]

separators = punctuators + ['\n']
operators = arithmetic + assignment + comparison + logical + bitwise + increment + [ternary]

S = ['Public int Main()\n', '{\n', '  int a = 7;\n', '  a++\n', '  while(a<S)\n', '   {\n', '     var str = "Hello World";\n', '     a--\n', '   }\n', '}']

lexeme = ""
words = []

for line in S:
    for char in line:
        if char in separators:
            if lexeme:
                words.append(lexeme)
            words.append(char)
            lexeme = ""
        elif char in single_comment:
            break  # Ignore the rest of the line for single-line comments
        elif char in multi_comment:
            lexeme += char
            if lexeme == multi_comment:
                lexeme = ""  # Ignore the rest of the line for multi-line comments
        elif char in operators:
            if lexeme:
                words.append(lexeme)
            lexeme = char
        else:
            lexeme += char

if lexeme:
    words.append(lexeme)

print(words)