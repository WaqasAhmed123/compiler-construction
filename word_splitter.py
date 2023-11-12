from docx import Document
import string

punctuators = ['{', '}', '(', ')', '[', ']', ';']
singleComment = "#"
multiComment = ' """'
arithmetic = ['+', '-', '*', '/', '//', '%']
assignment = ['+=', '-=', '*=', '/=', '%=']
comparison = ['==', '!=', '<', '>', '<=', '>=']
logical = ['&&', '||', '!']
bitwise = ['&', '|', '^', '~', '<<', '>>']
increment = ['++', '--']
ternary = '?'

class Token:
    def __init__(self):
        self.CP=None 
        self.VP =None
        self.LN =None

words = []

def customWordSplitter(text):
    currentWord = ""

    for char in text:
        # If the character is a letter or a digit, add it to the current word
        if char.isalnum() or char in string.punctuation:
            currentWord += char
        else:
            # If the current word is not empty, add it to the list of words
            if currentWord:
                words.append(currentWord)
                currentWord = ""

    # Add the last word if the text ends with a letter or digit
    if currentWord:
        words.append(currentWord)

    return words

# Read Word document content using open
documentPath = "word_splitter_doc.docx"
with open(documentPath, 'rb') as file:
    doc = Document(file)
    textFromDocument = ""
    for paragraph in doc.paragraphs:
        textFromDocument += paragraph.text + "\n"

# Use the custom word splitter
result = customWordSplitter(textFromDocument)

# Create instances of the Token class based on the words
Tokens = []
for word in words:
    t = Token()
    if(word in punctuators):
        t.CP="ID"
        t.VP=word
        t.LN="line"
    Tokens.append(t)
for token in Tokens:
    print(token.CP,token.VP,token.LN)
# print(words)
